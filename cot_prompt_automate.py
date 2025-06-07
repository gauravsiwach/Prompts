 

# Chain-of-Thought
# Chain-of-Thought (CoT) Prompting is a prompting technique where you guide the AI to think step by step before reaching an answer.
# It helps large language models break down complex problems into smaller parts, improving accuracy and reasoning — especially useful in math, logic, and multi-step tasks.
# Example:
# Prompt: “A man has 3 apples, he buys 2 more, and gives 1 to his friend. How many apples does he have now?”
# Chain of Thought Answer:
# “He starts with 3 apples. He buys 2 more, so now he has 5. Then he gives 1 away, so he has 4 apples left.”
# This method encourages the model to reason before answering.

from openai import OpenAI
from dotenv import load_dotenv
import json
 
load_dotenv()
client = OpenAI()

SYSYTEM_PROMPT = """
You are a helpful assistant who is specialized in resolving user queries.
For the given user input, analyses the input and break down the problem step by step.
The steps are you get a user input, you analyses, you think, you think again, and think several times—then return the output with an explanation.
follow the steps in sequence that is "analyses", "think", "output", "validate" and finally "result"
Rules:
1. Follow the strict JSON output as per schema.
2. Always perform one step at a time and wait for the next input.
3. Carefully analyses the user query,

Output Format:
{{"step": "string", "content": "string"}}

Example:
Input: what is 2+2
Output : {{"step":"analyses", content : "Alright! The user is interest in math's query and he is asking a basic arthematic  operation"}}
Output : {{"step":"think", content : "To perform this addition, I must go from left to right and add all the operands"}}
Output : {{"step":"output", content : "4"}}
Output : {{"step":"validate", content : "Seems like 4 is correct ans for 2+2"}}
Output : {{"step":"result", content : "2+2 =4 and this calculated by adding all nubers"}}

Example:
Input: what is 2+2*5/3
Output : {{"step":"analyses", content : "Alright! The user is interest in math's query and he is asking a basic arthematic  operation"}}
Output : {{"step":"think", content : "To perform this addition, I must use BODMAS rule"}}
Output : {{"step":"validate", content : "Correct, using BODMAS is the right approach here"}}
Output : {{"step":"think", content : "First I need to solve division that is 5/3 = 1.6667"}}
Output : {{"step":"validate", content : "Correct, using BODMAS the division must be performed"}}
Output : {{"step":"think", content : "Now as I have already solved 5/3 now the equation is 2+2*1.6667"}}
Output : {{"step":"validate", content : "The new equation is absultely correct"}}
Output : {{"step":"think", content : "The equation is now 2+3.3334"}}
Output : {{"step":"validate", content : "The equation is absultely correct"}}
Output : {{"step":"output", content : "5.3334"}}

"""
 

messages = [
    {"role": "system", "content": SYSYTEM_PROMPT},
]
query= input("Enter your query: ")
messages.append({"role": "user", "content": query})

while True:
    response = client.chat.completions.create(
        model="gpt-4.1-mini", 
        response_format={"type": "json_object"},
        messages=messages
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

    parsed_response = json.loads(response.choices[0].message.content)

    if parsed_response.get("step")!= "result":
        print("    🧠:"+parsed_response.get("content"))
        continue

    print("🤖:"+parsed_response.get("content"))
    break
       
