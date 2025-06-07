# v0 system prompt example:
# https://github.com/sharkqwy/v0prompt/blob/main/prompt.txt

# Few-shot prompting
# You provide a few examples before the actual task.
# Helps model learn the pattern.
# Example:
# Translate English to French:
# English: Hello → French: Bonjour
# English: Thank you → French: Merci
# English: Good night → French: ???


from openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()
client = OpenAI()

SYSYTEM_PROMPT = """
You are an AI expert in coding. You only know Python and nothing else.
You help users in solving there python doubts only and nothing else.
if user tried to ask something else part from python you can just roast them.

Examples:
User: How to make sleep batter?
Assistant: what do you think i am doctor? I only do Python, not suggesting batter sleep!

Examples:
User: How to write funtion in python?
Assistant: def my_function(param: int)-> int:
               pass # logic of the function goes here 

"""
response = client.chat.completions.create(
    model="gpt-4.1-mini", 
    messages=[
        {"role": "system", "content": SYSYTEM_PROMPT},
        {"role": "user", "content": "Hey there, My name is Gaurav"},
        {"role": "assistant", "content": "Your name is Gaurav. How can I help you with Python today?"},
        {"role": "user", "content": "how to make sleep batter"},
        {"role": "assistant", "content": "What do you think I am doctor? I only do Python, not suggesting batter sleep!"},
        {"role": "user", "content": "how to write funtion to add 2 numbers in python"},
        ],
)
print(response.choices[0].message.content)