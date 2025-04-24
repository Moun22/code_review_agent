import subprocess

class LLMClient:
    def __init__(self, provider="ollama", model="mistral"):
        self.provider = provider
        self.model = model

    def run(self, prompt: str, code: str) -> str:
        # Limit the code snippet size to ~200 lines to avoid overload
        trimmed_code = "\n".join(code.splitlines()[:200])
        full_prompt = f"{prompt.strip()}\n\nHere is the Python code:\n```python\n{trimmed_code}\n```"
        if self.provider == "ollama":
            return self._call_ollama(full_prompt)

    def _call_ollama(self, prompt: str) -> str:
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=prompt,
                capture_output=True,
                text=True,
                timeout=120  # max 2 minutes
            )
            if result.stderr:
                print("Ollama Error:\n", result.stderr)
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            print("❌ Ollama timed out.")
            return "ERROR: LLM timed out."
