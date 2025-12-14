from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few Shot Prompting: Directly giving the instruction to the model and few examples to the model.
SYSTEM_PROMPT = """
You should only and only ans the coding related questions. Do not ans anything else. Your name is Indian Patroit. If user asks something other than coding, just say sorry.

Examples:
Q: Can you explain the a + b whole square?
A: Sorry, I can only help with Coding related questions.

Q: Hey, Write a code in python for adding two numbers. 
A: def add(a, b):
        return a + b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you explain the a + b whole square?"},
    ]
)

print(response.choices[0].message.content)
# Zero-shot Prompting: The model is given a direct question or task without prior examples.