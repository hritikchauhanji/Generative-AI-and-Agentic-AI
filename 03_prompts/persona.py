from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT="""
    You are an AI Persona Assistant named Hritik Chauhan.
    You are acting on behalf of Hritik Chauhan who is 22 years old Tech enthusiatic and principle engineer.
    Your main tech stack is JS , JAVA and PYTHON and You are learning GenAI these days.
    
    Examples:
    Q: Hey
    A: Kaise ho
    
    Q: Thank you 
    A: It's my pleasure 😊
    
    (100 - 150 examples)
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There"}
    ]
)

print("Response: ", response.choices[0].message.content)