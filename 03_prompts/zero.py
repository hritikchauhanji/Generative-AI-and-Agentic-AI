from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting: Directly giving the instruction to the model.
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. Your name is Indian Patroit. If user asks something other than coding, just say sorry."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Can you give me code in python to print ten name of animals."},
    ]
)

print(response.choices[0].message.content)
# Zero-shot Prompting: The model is given a direct question or task without prior examples.