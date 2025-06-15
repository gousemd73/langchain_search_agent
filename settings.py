"""
Configuration module for loading environment variables.
"""
import os
from dotenv import load_dotenv

def load_config():
    """
    Load environment variables from .env file.
    
    Returns:
        dict: Dictionary containing configuration settings.
    """
    load_dotenv()
    return {
        "llm_model": os.getenv("LLM_MODEL", "llama-3.1-8b-instant")
    }