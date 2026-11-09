import os
from dotenv import load_dotenv

# from amthropic import Amthropic
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"],
)

model = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] 

def main():
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    while True:
        prompt = input("You: ").strip()
        if prompt.lower() in {"exit", "quit", "goodbye"}:
            print("AI Assistant: Goodbye!")
            break

        messages.append({"role": "user", "content": prompt })
        response = client.chat.completions.create(model=model, messages=messages)
        message = client.chat.completions.create(
            model=model,
            #max_tokens=4096,
            max_completion_tokens=4096,
            messages= messages)
    
        reply = message.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"AI Assistant: {reply}")

        # messages.append({"role": "user", "content": prompt})
        # response = client.chat.completions.create(model=model, messages=messages)

        # reply = response.choices[0].message.content
        # messages.append({"role": "assistant", "content": reply})
        # print(f"Bot: {reply}")

if __name__ == "__main__":
    main()