"""
Figma API integration for UX Audit Studio.
Extracts frames and components from Figma URLs via Figma REST API.
"""

import re
import io
import logging
import requests
from typing import Optional, List, Dict, Any, Tuple
from PIL import Image

logger = logging.getLogger(__name__)


def parse_figma_url(url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract file_key and optional node_id from a Figma URL.
    Supports formats:
    - https://www.figma.com/design/:file_key/:title?node-id=10-24
    - https://www.figma.com/file/:file_key/:title?node-id=10%3A24
    - https://www.figma.com/proto/:file_key/:title?node-id=10:24
    """
    if not url:
        return None, None

    url = url.strip()

    # Extract file_key (letters, numbers, underscores)
    file_match = re.search(r"figma\.com/(?:file|design|proto)/([a-zA-Z0-9]+)", url)
    file_key = file_match.group(1) if file_match else None

    # Extract node_id
    node_id = None
    node_match = re.search(r"node-id=([a-zA-Z0-9\-_%:]+)", url)
    if node_match:
        raw_id = node_match.group(1)
        # Decode %3A or %3a to :
        raw_id = raw_id.replace("%3A", ":").replace("%3a", ":")
        # Replace hyphens with colons (Figma URL query uses '-' instead of ':')
        raw_id = raw_id.replace("-", ":")
        node_id = raw_id

    return file_key, node_id


def fetch_figma_node_image(
    file_key: str,
    node_id: str,
    figma_token: str,
    scale: int = 2,
    timeout: float = 30.0,
) -> Tuple[Optional[Image.Image], Optional[str]]:
    """
    Fetch a rendered PNG image of a specific node/frame from Figma API.
    Returns (Image, error_message).
    """
    if not file_key or not node_id:
        return None, "Thiếu file_key hoặc node_id từ đường dẫn Figma."
    if not figma_token:
        return None, "Chưa cung cấp Figma Personal Access Token."

    api_url = f"https://api.figma.com/v1/images/{file_key}"
    headers = {"X-Figma-Token": figma_token.strip()}
    params = {"ids": node_id, "format": "png", "scale": scale}

    try:
        response = requests.get(api_url, headers=headers, params=params, timeout=timeout)
        if response.status_code == 403:
            return None, "Figma Token không hợp lệ hoặc không có quyền xem file này."
        elif response.status_code == 404:
            return None, "Không tìm thấy file hoặc frame tương ứng trên Figma."
        elif response.status_code != 200:
            return None, f"Lỗi từ Figma API ({response.status_code}): {response.text}"

        data = response.json()
        images_dict = data.get("images", {})
        image_url = images_dict.get(node_id)

        if not image_url:
            return None, f"Figma không xuất được ảnh cho node-id: {node_id} (Có thể là node ẩn hoặc rỗng)."

        # Download rendered PNG bytes
        img_response = requests.get(image_url, timeout=timeout)
        if img_response.status_code == 200:
            image = Image.open(io.BytesIO(img_response.content))
            return image, None
        else:
            return None, f"Không thể tải ảnh render từ CDN Figma ({img_response.status_code})."

    except requests.exceptions.Timeout:
        return None, "Quá thời gian kết nối tới Figma API (Timeout)."
    except Exception as e:
        logger.error(f"Error fetching Figma image: {e}")
        return None, f"Lỗi xử lý kết nối: {str(e)}"


def list_figma_file_frames(
    file_key: str,
    figma_token: str,
    timeout: float = 30.0,
) -> Tuple[List[Dict[str, str]], Optional[str]]:
    """
    List all top-level frames/screens in a Figma file for selection.
    Returns (List of frames [{'id': '1:2', 'name': 'Login', 'page': 'Home'}], error_message).
    """
    if not file_key or not figma_token:
        return [], "Thiếu file_key hoặc Figma Access Token."

    api_url = f"https://api.figma.com/v1/files/{file_key}?depth=2"
    headers = {"X-Figma-Token": figma_token.strip()}

    try:
        response = requests.get(api_url, headers=headers, timeout=timeout)
        if response.status_code != 200:
            return [], f"Lỗi Figma API ({response.status_code}): {response.text}"

        data = response.json()
        frames = []
        document = data.get("document", {})
        for page in document.get("children", []):
            page_name = page.get("name", "Trang thiết kế")
            for child in page.get("children", []):
                child_type = child.get("type", "")
                if child_type in ("FRAME", "COMPONENT", "SECTION"):
                    frames.append({
                        "id": child.get("id"),
                        "name": child.get("name", "Frame không tên"),
                        "page": page_name,
                        "type": child_type,
                    })

        return frames, None
    except Exception as e:
        logger.error(f"Error fetching Figma file frames: {e}")
        return [], f"Lỗi khi lấy danh sách frame: {str(e)}"
