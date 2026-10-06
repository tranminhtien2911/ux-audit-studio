"""
Bridge to interact with Gemini NotebookLM MCP and service layer.
"""

import sys
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

DEFAULT_NOTEBOOK_ID = "5978c8ed-b6a7-4d2a-8793-fc2f6a025ac7"  # The Design of Everyday Creative Things


def get_nlm_client(profile: str = "default"):
    """Initialize and return an authenticated NotebookLMClient."""
    try:
        import os
        # Support Streamlit secrets for Cloud deployment
        try:
            import streamlit as st
            if hasattr(st, "secrets") and "NOTEBOOKLM_COOKIES" in st.secrets:
                if not os.environ.get("NOTEBOOKLM_COOKIES"):
                    os.environ["NOTEBOOKLM_COOKIES"] = st.secrets["NOTEBOOKLM_COOKIES"]
        except Exception:
            pass

        from notebooklm_tools.cli.utils import get_client

        # If NOTEBOOKLM_COOKIES environment variable is present, use it
        if os.environ.get("NOTEBOOKLM_COOKIES"):
            return get_client(profile=None)

        # Check if local profile exists before calling get_client to avoid process exit on headless cloud
        from notebooklm_tools.services.auth import AuthManager
        target_profile = profile or "default"
        if not AuthManager(target_profile).profile_exists():
            return None

        return get_client(profile=target_profile)
    except BaseException as e:
        logger.warning(f"Failed to initialize NotebookLM client: {e}")
        return None


def fetch_notebooks(profile: str = "default") -> List[Dict[str, Any]]:
    """Fetch the list of notebooks in the user's account."""
    try:
        from notebooklm_tools.services import notebooks as notebook_service
        client = get_nlm_client(profile)
        if not client:
            return []
        with client:
            result = notebook_service.list_notebooks(client)
            return result.get("notebooks", [])
    except BaseException as e:
        logger.warning(f"Error fetching notebooks: {e}")
        return []


def query_notebook_knowledge(
    question: str,
    notebook_id: str = DEFAULT_NOTEBOOK_ID,
    profile: str = "default",
    timeout: float = 60.0,
) -> Optional[Dict[str, Any]]:
    """
    Query grounded design principles from the NotebookLM notebook.
    Returns the answer and cited sources.
    """
    try:
        from notebooklm_tools.services import chat as chat_service
        client = get_nlm_client(profile)
        if not client:
            return None
        with client:
            result = chat_service.query(
                client=client,
                notebook_id=notebook_id,
                query_text=question,
                timeout=timeout,
            )
            return result
    except BaseException as e:
        logger.warning(f"Error querying notebook {notebook_id}: {e}")
        return None

