import argparse
from agent.analyzer import review_code

def load_code(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def save_review(output: str, path="reviews/review_output.md"):
    with open(path, "w") as f:
        f.write(output)

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("--file", required=True, help="Path to Python file")
    parser.add_argument("--mode", default="strict", choices=["strict", "mentor", "test_focus"])
    parser.add_argument("--provider", default="ollama", choices=["ollama"])
    args = parser.parse_args()

    code = load_code(args.file)

    print("🔍 Loading and preparing prompt...")
    review = review_code(code, args.mode, args.provider)

    print("✅ Review completed. Saving to file...")
    save_review(review)

    print("\n🎉 Done! See: reviews/review_output.md")


if __name__ == "__main__":
    main()
 
