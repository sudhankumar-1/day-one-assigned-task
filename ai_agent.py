import os
import sys
import json
import csv
from groq import Groq

# Ensure UTF-8 output
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def read_expenses_csv():
    """Reads the expenses CSV file and returns its content as a string."""
    try:
        with open("expenses.csv", mode="r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: expenses.csv not found."

def run_ai_agent(query):
    print("--- AI Agent ---")
    print(f"User Query: {query}")
    
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Please set the GROQ_API_KEY environment variable.")
        return
    client = Groq(api_key=api_key)
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "read_expenses_csv",
                "description": "Reads the user's private expenses.csv file and returns the data.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }
    ]
    
    messages = [
        {"role": "system", "content": "You are a helpful AI agent with access to the user's private expenses data via tools. You must use the tool to read the data if the user asks about their expenses."},
        {"role": "user", "content": query}
    ]
    
    # Loop for agent reasoning and tool use
    max_iterations = 3
    for _ in range(max_iterations):
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        
        response_message = response.choices[0].message
        
        if response_message.tool_calls:
            print("Agent is calling a tool...")
            messages.append(response_message)
            
            for tool_call in response_message.tool_calls:
                if tool_call.function.name == "read_expenses_csv":
                    print(f"Executing tool: {tool_call.function.name}")
                    function_response = read_expenses_csv()
                    messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": tool_call.function.name,
                            "content": function_response,
                        }
                    )
        else:
            print("Agent Final Response:")
            print(response_message.content)
            break

if __name__ == "__main__":
    query = "How much did I spend on food this month according to my expenses?"
    run_ai_agent(query)
