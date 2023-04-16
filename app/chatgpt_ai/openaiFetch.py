from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        temperature =  1,
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        promt_response = response_dict[0]["message"]["content"]
    
    return promt_response
