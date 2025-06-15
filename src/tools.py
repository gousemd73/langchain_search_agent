"""
Module for initializing search tools.
"""
from langchain_community.tools import DuckDuckGoSearchRun
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_search_tool() -> DuckDuckGoSearchRun:
    """
    Initialize the DuckDuckGo search tool.

    Returns:
        DuckDuckGoSearchRun: Initialized search tool instance.

    Raises:
        Exception: If tool initialization fails.
    """
    try:
        search_tool = DuckDuckGoSearchRun()
        logger.info("Successfully initialized DuckDuckGo search tool")
        return search_tool
    except Exception as e:
        logger.error(f"Failed to initialize search tool: {str(e)}")
        raise
