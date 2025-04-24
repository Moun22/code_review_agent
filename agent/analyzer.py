import yaml
from agent.llm_interface import LLMClient

def load_prompt(mode: str) -> str:
    with open("prompts/templates.yaml", "r") as f:
        templates = yaml.safe_load(f)
    return templates.get(mode, {}).get("description", "")

def review_code(code: str, mode: str, provider: str = "ollama") -> str:
    prompt = load_prompt(mode)
    llm = LLMClient(provider=provider)
    response = llm.run(prompt, code)
    return response
