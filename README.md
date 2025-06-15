# WTC Final Query Application

This is a capstone project that queries the teams playing in the World Test Championship (WTC) final using a ReAct agent powered by LangChain and Grok.

## Project Structure
- `config/settings.py`: Handles environment variable loading.
- `src/llm.py`: Initializes the language model.
- `src/tools.py`: Initializes the DuckDuckGo search tool.
- `src/agent.py`: Creates and executes the ReAct agent.
- `main.py`: Main script to run the application.
- `.env`: Environment variable configuration.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.

## Prerequisites
- Python 3.8+
- Install dependencies: `pip install -r requirements.txt`
- Create a `.env` file with the required environment variables (see `.env` example).

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up the `.env` file with the appropriate configuration.
4. Run the application: `python main.py`.

## Usage
The application queries the teams playing in the WTC final for the current day and outputs their names.

## License
MIT License
