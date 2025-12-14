from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "I am Hritik Chauhan."},
    ]
)

print(response.choices[0].message.content)