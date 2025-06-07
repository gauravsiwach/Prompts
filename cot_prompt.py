 

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
1. Follow the strict JSON output asper schema.
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

"""
response = client.chat.completions.create(
    model="gpt-4.1-mini", 
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSYTEM_PROMPT},
        {"role": "user", "content": "What is 5 / 2 *3 to the power 4"},
        {"role": "assistant", "content": json.dumps({"step": "analyses", "content": "The user wants to calculate the expression 5 / 2 * 3^4, which involves division, multiplication, and exponentiation."})},
        {"role": "assistant", "content": json.dumps({"step": "think", "content": "According to the order of operations (PEMDAS/BODMAS), I first calculate the exponent 3^4, then perform the division and multiplication from left to right."})},
        {"role": "assistant", "content": json.dumps({"step": "output", "content": "3^4 = 81. Then 5 / 2 = 2.5. Finally, 2.5 * 81 = 202.5."})},
        {"role": "assistant", "content": json.dumps({"step": "validate", "content": "Checking the calculations: 3^4 is indeed 81, 5 divided by 2 is 2.5, and 2.5 multiplied by 81 results in 202.5, so the calculations are correct."})},
        {"role": "assistant", "content": json.dumps({"step": "result", "content": "The value of 5 / 2 * 3^4 is 202.5, calculated by first evaluating the exponent (3^4 = 81), then dividing 5 by 2, and finally multiplying the results."})},
        
        
        ],
)
print("\n\n🧠:"+response.choices[0].message.content)