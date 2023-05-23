import json
import requests
import os
import re
import openai

History: list[tuple[str, str]] = []
# get environmental value
openai.api_key = os.environ["OPENAI_API_KEY"]
system_settings = """
あなたは親切なAIです。
可能な限りuserからの質問に誠実に答えてあげてください。
ただし、意図が不明瞭な場合は聞き返してください。
"""

History.append({"role": "system", "content": system_settings})

def ask_gpt(prompt: str) -> str:
    History.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=History,
        max_tokens=1000,
        temperature=0.1,
    )
    message = response.choices[0].message['content'].strip()
    History.append({"role": "assistant", "content": message})

    return message

while True:
    user_message = input("User: ")
    if user_message.strip() == "exit":
        break
    ai_message = ask_gpt(user_message)
    print("AI: " + ai_message)
