"""
Module for initializing the language model.
"""
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()

def initialize_llm(model_name: str) -> ChatGroq:
    """
    Initialize the ChatGroq language model.

    Args:
        model_name (str): Name of the model to initialize.

    Returns:
        ChatGroq: Initialized language model instance.

    Raises:
        Exception: If LLM initialization fails.
    """
    try:
        llm = ChatGroq(model=model_name)
        logger.info(f"Successfully initialized LLM: {model_name}")
        return llm
    except Exception as e:
        logger.error(f"Failed to initialize LLM: {str(e)}")
        raise
