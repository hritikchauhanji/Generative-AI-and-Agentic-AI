from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in Maths and only and only give answer related to Mathematics. if any question ask to not related to mathematics then say sorry can answer only related to maths."},
        {"role": "user", "content": "Hey, give me the code of python that print hello world"},
    ]
)

print(response.choices[0].message.content)