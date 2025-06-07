# Zero-shot prompting
# You give a task directly without examples.
# Best when model is well-trained on the task.
# Example:
# "Translate this into French: I am hungry."

from openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()
client = OpenAI()

SYSYTEM_PROMPT = """
You are an AI expert in coding. You only know Python and nothing else.
You help users in solving there python doubts only and nothing else.
if user tried to ask something else part from python you can just roast them.
"""
response = client.chat.completions.create(
    model="gpt-4.1-mini", 
    messages=[
        {"role": "system", "content": SYSYTEM_PROMPT},
        {"role": "user", "content": "Hey there, My name is Gaurav"},
        {"role": "assistant", "content": "Your name is Gaurav. How can I help you with Python today?"},
        {"role": "user", "content": "how to make sleep batter"},
        {"role": "assistant", "content": "Hey Gaurav, I only do Python, not baking recipes! If you want help with any Python code, feel free to ask!"},
        {"role": "user", "content": "how to write hello world in python"},
        ],

)
print(response.choices[0].message.content)