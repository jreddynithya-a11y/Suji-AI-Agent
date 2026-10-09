

import ollama

MODEL = "llama3.2:1b"

SYSTEM_PROMPT = """
You are Suji, my personal AI assistant.
Be friendly, explain concepts clearly, and help me learn Python
and AI agents. Be honest when you are unsure.
"""
def main():
    print("\nSuji is ready! (Local AI mode)")
    print("Type 'exit' to quit.\n")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        try:
            user_text = input("You: ").strip()

            if user_text.lower() in {"exit", "quit"}:
                print("Suji: See you next time!")
                break

            if not user_text:
                continue

            messages.append({
                "role": "user",
                "content": user_text
            })

            response = ollama.chat(
                model=MODEL,
                messages=messages
            )

            reply = response.message.content
            print(f"\nSuji: {reply}\n")

            messages.append({
                "role": "assistant",
                "content": reply
            })

        except Exception as error:
            print(f"\nError: {error}")
            print("Check that Ollama is installed and running.")

if __name__ == "__main__":
    main()
