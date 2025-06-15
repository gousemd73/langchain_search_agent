import logging
from settings import load_config
from src.llm import initialize_llm
from src.tools import initialize_search_tool
from src.agent import create_agent, execute_agent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to initialize and run the WTC Final query application.
    """
    try:
        # Load configuration
        config = load_config()
        model_name = config["llm_model"]

        # Initialize components
        llm = initialize_llm(model_name)
        search_tool = initialize_search_tool()
        agent_executor = create_agent(llm, [search_tool])

        # Execute query
        query = "Who are playing WTC final today? just give me name of teams"
        response = execute_agent(agent_executor, query)
        
        # Print result
        print(response["output"])
        
    except Exception as e:
        logger.error(f"Application failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
