import argparse
import os
import ollama

def load_code(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_prompt(task: str, main_code: str, context_code: str = "") -> str:
    prompt = f"""You are a senior software engineer assistant helping with code analysis and understanding.
                ## Task:
                    {task}
                ## Instructions:
                    - Carefully review the following code.
                    - If context is provided, use it to enhance your understanding.
                    - Provide a detailed, accurate, and structured response.
                    - Avoid unnecessary explanations if not requested.
                """
    if context_code.strip():
        prompt += f"""## Context Code (supporting modules, functions, or classes):
                        {context_code.strip()}
                    """
        
    prompt += f"""## Main Code (primary target of this analysis):
                    {main_code.strip()}
                 ### Now respond to the task above.
                """
    return prompt

def call_ollama(prompt: str, model: str = "deepseek-coder:latest") -> str:
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"⚠️ Error running Ollama: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Local Coding Assistant (CLI via Ollama)")
    parser.add_argument("--main", required=True, help="Path to the main code file")
    parser.add_argument("--context", help="Path to context file (optional)", default="")
    parser.add_argument("--task", required=True, help="Task to perform (e.g., explain, refactor, test)")
    parser.add_argument("--model", help="Ollama model to use (default: deepseek-coder:latest)", default="deepseek-coder:latest")

    args = parser.parse_args()

    main_code = load_code(args.main)
    context_code = load_code(args.context) if args.context else ""
    prompt = generate_prompt(args.task, main_code, context_code)

    print("\n🧠 Generated Prompt:\n")
    print(prompt)

    print("\n🤖 Generating response from model...\n")
    response = call_ollama(prompt, args.model)

    print("\n📄 Model Output:\n")
    print(response)

if __name__ == "__main__":
    main()

# python codepilot.py --main C:\Users\nikhi\Documents\Projects\Question-Answer-Platform\src\main\java\com\question\controller\QuestionController.java --task "Explain getQuestionsById method."

