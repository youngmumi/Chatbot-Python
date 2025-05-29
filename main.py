import os
import openai
from dotenv import load_dotenv

# .env 파일에서 API 키 불러오기
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"[오류 발생] {e}"

def main():
    print("💬 GPT-3.5 콘솔 챗봇입니다. 'exit'을 입력하면 종료됩니다.")
    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "exit":
            print("👋 챗봇을 종료합니다.")
            break
        response = chat_with_gpt(user_input)
        print(f"🤖 Chatbot: {response}")

if __name__ == "__main__":
    main()
