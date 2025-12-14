from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    
    Rules:
    - Strickly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times)
    and finally OUTPUT (which is going to the displayed to the user).
    
    Output JSON Format:
    { "step": "START | "PLAN" | "OUTPUT", "content": "string" }
    
    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10 
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "loolking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5" }
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT", "content": "3.5" }
"""
                
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Write a code in python for adding n numbers"},
        {"role": "assistant", "content": json.dumps({
            "step": "START",
            "content": "Write a code in python for adding n numbers"
        })},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a Python code snippet to add 'n' numbers. I should provide a function that takes a collection of numbers and returns their sum."})},
        {"role": "assistant", "content": json.dumps({
  "step": "PLAN",
  "content": "I will define a Python function that uses `*args` to accept an arbitrary number of numerical arguments. Inside the function, I will iterate through these arguments and sum them up, then return the total. I will also include an example of how to call the function."
})},
    ]
)

print(response.choices[0].message.content)