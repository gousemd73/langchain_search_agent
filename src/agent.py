"""
Module for creating and executing the ReAct agent.
"""
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_agent(llm: BaseLanguageModel, tools: list[BaseTool]) -> AgentExecutor:
    """
    Create and configure the ReAct agent with the given LLM and tools.

    Args:
        llm (BaseLanguageModel): The language model instance.
        tools (list[BaseTool]): List of tools to be used by the agent.

    Returns:
        AgentExecutor: Configured agent executor instance.

    Raises:
        Exception: If agent creation fails.
    """
    try:
        prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        logger.info("Successfully created ReAct agent")
        return agent_executor
    except Exception as e:
        logger.error(f"Failed to create agent: {str(e)}")
        raise

def execute_agent(agent_executor: AgentExecutor, query: str) -> dict:
    """
    Execute the agent with the provided query.

    Args:
        agent_executor (AgentExecutor): The agent executor instance.
        query (str): The query to execute.

    Returns:
        dict: Response from the agent.

    Raises:
        Exception: If agent execution fails.
    """
    try:
        response = agent_executor.invoke({"input": query})
        logger.info("Successfully executed agent query")
        return response
    except Exception as e:
        logger.error(f"Failed to execute agent query: {str(e)}")
        raise