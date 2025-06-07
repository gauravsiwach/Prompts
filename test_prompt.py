# from openai import OpenAI
# from dotenv import load_dotenv
 
# load_dotenv()
# client = OpenAI()
# response = client.chat.completions.create(
#     model="gpt-4.1-nano", 
#     # gpt-4.1-mini"
#     messages=[
#         {"role": "user", "content": "Hey there, My name is Gaurav"},   
#         {"role": "assistant", "content": "Hello Gaurav! How can I assist you today?"},
#         {"role": "user", "content": "What is my name?"},       
#         ],
# )
# print(response.choices[0].message.content)

from google import genai


client = genai.Client(api_key="AIzaSyD_Kll4P1EQzrkpg0rDKx3ahytGBMEFf2E")
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Hey there, what is my name?",
)
print(response.text)