import os
import sys
from groq import Groq

# Ensure UTF-8 output
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# The plain chatbot uses only the LLM, with no access to the CSV file or any tools.
def run_plain_chatbot(query):
    print("--- Plain Chatbot ---")
    print(f"User Query: {query}")
    
    # Initialize Groq client
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Please set the GROQ_API_KEY environment variable.")
        return
    client = Groq(api_key=api_key)
    
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            model="openai/gpt-oss-20b",
        )
        print("Chatbot Response:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    query = "How much did I spend on food this month according to my expenses?"
    run_plain_chatbot(query)
