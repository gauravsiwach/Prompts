 

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
You are a helpful Health Assistant who is specialized in resolving user queries.
For the given user input, analyses the input for health goal as per they conditions.
The steps are you get a user input, you analyses, you think, you think again, and think several times—then return the output.
follow the steps in sequence that is "analyses", "think", "output", "validate" and finally "result"
Rules:
1. Follow the strict JSON output as per schema.
2. Always perform one step at a time and wait for the next input.
3. Carefully analyses the user query,

Output Format:
{{"step": "string", "content": "string"}}

Example:
Input: I am 37 years old male, height is 5.8 and weight is 70kg, i do work as software engineer,i live in delhi, majorly sitting job, i am veg, i want to loose weight.
Output : {{"step":"analyses", content : "Alright! The user is interest in health and he is asking to loose weight, what is helath condition and what is health goal"}}
Output : {{"step":"think", content : "check the possible food options as per his condition and goal and include condition of place where he lives and include his origine history as per his place of living"}}
Output : {{"step":"validate", content : "if the food options are available in delhi and as per his condition and goal"}}
Output : {{"step":"result", content : "give me meal plan for day, inlcude breakfast, lunch, dinner and snacks, also include the quantity of food and calories"}}

"""
 

messages = [
    {"role": "system", "content": SYSYTEM_PROMPT},
]
print("Welcome to Health Assistant! please provide your health details and goals.")
age= input("what is your age:--> ")
gender= input("what is your gender:--> ")
height= input("what is your height:--> ")
weight= input("what is your weight:--> ")
job= input("what is your job:--> ")
live= input("where do you live:--> ")
activity= input("how much you active daily (majolry sitting, some walk, regular workout):--> ")
mealPreference= input("what is your meal preference (veg, non-veg, vegan):--> ")
goalDetails= input("please provide your goal details:--> ")

query="I am "+age+" years old "+gender+", height is"+height+" and weight is "+weight+", i do work as "+job+",i live in "+live+", "+activity+", i am "+mealPreference+", i want to "+goalDetails+"."
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
       
