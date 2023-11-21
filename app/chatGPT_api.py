#this is the file for the chatGPT API.
from openai import OpenAI
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
print(OpenAI.api_key)


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)