from openai import OpenAI
import os
from dotenv import load_dotenv
from function_call.tools import tools

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_msg = "You are a helpful assistant that will extract one keyword from the users input to pass into an API"

def filter_user_input(user_input):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages =[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_input}
        ],
        tools=tools
    )

    return response
    
