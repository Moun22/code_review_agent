<!-- Create a README for an AI Code Review Agent. Describe:
- What it does
- How it works
- CLI usage examples
- Provider options (openai, ollama, anthropic)
- Prompt modes (strict, mentor, test_focus)
-->
# AI Code Review Agent

## What it does
The AI Code Review Agent is a specialized tool designed to assist developers in reviewing code. It leverages advanced AI models to analyze code snippets, provide feedback, suggest improvements, and identify potential issues or bugs.

## How it works
The agent utilizes various AI models that can understand and analyze code. Depending on the selected provider, the agent can offer different levels of insights and suggestions. The agent can be configured to operate in different modes, each tailored for specific review scenarios.

## CLI Usage Examples
1. **Basic Code Review**
   ```bash
   ai_code_review --file path/to/code.py
   ```

2. **Review with Specific Provider**
   ```bash
   ai_code_review --file path/to/code.py --provider openai
   ```

3. **Change Prompt Mode**
   ```bash
   ai_code_review --file path/to/code.py --prompt_mode mentor
   ```

4. **Generate Report**
   ```bash
   ai_code_review --file path/to/code.py --report
   ```

## Provider Options
- **OpenAI**: Utilizes OpenAI's GPT models for detailed code analysis and suggestions.
- **Ollama**: Leverages Ollama's models for a more conversational approach to code review.
- **Anthropic**: Focuses on ethical AI practices while providing code insights.

## Prompt Modes
- **Strict**: Provides a focused review with minimal context