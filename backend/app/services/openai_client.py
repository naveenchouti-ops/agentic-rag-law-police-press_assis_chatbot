import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_openai(system_prompt, user_message, memory=None):
    try:
        messages = []

        if memory:
            messages.extend(memory)

        messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as e:
        print("🔥 OpenAI ERROR:", e)
        return "⚠️ AI response failed. Please try again."


































































# def ask_openai(system_prompt: str, user_message: str, memory=None) -> str:
#     messages = []

#     # 🧠 past conversation (memory)
#     if memory:
#         messages.extend(memory)

#     # 🧾 system + user message
#     messages.append({"role": "system", "content": system_prompt})
#     messages.append({"role": "user", "content": user_message})

#     # 🤖 OpenAI call
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",   # or gpt-4.1-mini
#         messages=messages,
#         temperature=0.4
#     )

#     return response.choices[0].message.content
