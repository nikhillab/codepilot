from agno.models.ollama import Ollama


def model() -> Ollama:
    return Ollama(id="deepseek-coder:latest")