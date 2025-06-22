import argparse
from agents.test_generator_agent import test_generator_agent
from agents.code_explainer_agent import code_explainer_agent
from agents.code_generator_agent import code_generator_agent

AGENTS = {
    "test": test_generator_agent,
    "explain": code_explainer_agent,
    "generate": code_generator_agent,
}

def load_file(path):
    with open(path, "r") as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Run local code agent with task input")
    parser.add_argument("--main", required=True, help="Path to main code file")
    parser.add_argument("--context", help="Path to context code file (optional)")
    parser.add_argument("--agent", choices=AGENTS.keys(), required=True, help="Agent to run")

    args = parser.parse_args()
    main_code = load_file(args.main)
    context_code = load_file(args.context) if args.context else ""
    
    agent = AGENTS[args.agent]
    print(agent)
    result = agent.run(
       message=main_code
    )
    
    print("\n📄 Result:\n")
    print(result.content)

if __name__ == "__main__":
    main()

# python main.py --main C:\Users\nikhi\Documents\Projects\Question-Answer-Platform\src\main\java\com\question\controller\QuestionController.java --agent "explain"
