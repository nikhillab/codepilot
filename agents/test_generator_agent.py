from agno.agent import Agent

from agno.models.ollama import Ollama

test_generator_agent = Agent(
    model=Ollama(id="deepseek-coder:latest"),
    agent_id="Test Generator",
    description="You are a test-writing expert with deep experience in unittest, BDD and TDD.",
    goal="Generate complete and clear test cases for the provided code using best practices.",
    debug_mode=True
)
