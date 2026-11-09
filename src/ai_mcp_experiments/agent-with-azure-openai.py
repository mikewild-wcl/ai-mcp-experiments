# This just connects to Azure OpenAI and runs a chat loop
# It is intended to prove the connectivity only.
# Use agent.py if you want to run the client from the book.

import os
from dotenv import load_dotenv

# from amthropic import Amthropic
from openai import OpenAI

load_dotenv()

# print(os.environ["AZURE_OPENAI_API_KEY"])
# print(os.environ["AZURE_OPENAI_ENDPOINT"])

# print(os.environ["AZURE_OPENAI_API_KEY"])
# print(os.environ["AZURE_OPENAI_ENDPOINT"])

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
)

model = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] 
print(f"Endpoint: {os.environ['AZURE_OPENAI_ENDPOINT']} Model: {model}")

# Chat loop to prove connectivity works (from Claude)
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(model=model, messages=messages)

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Bot: {reply}")