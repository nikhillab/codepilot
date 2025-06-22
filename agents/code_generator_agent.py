from agno.agent import Agent

from agno.models.ollama import Ollama

code_generator_agent = Agent(
    model=Ollama(id="deepseek-coder:latest"),
    agent_id="Code Generator",
    description="You are a productive software engineer who translates natural language tasks into code.",
    goal="Given a task description and any helpful context code, generate production-ready code to fulfill the request.",
    debug_mode=True,
)
