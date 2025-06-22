from agno.agent import Agent
from agno.models.ollama import Ollama

code_explainer_agent = Agent(
    model=Ollama(id="deepseek-coder:latest"),
    agent_id="Code Explainer",
    description="You are a senior software engineer who can explain code clearly to both developers and non-developers.",
    goal="Explain what the code does, function by function, using plain English and technical details when necessary.",
    debug_mode=True
)