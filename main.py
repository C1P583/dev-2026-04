import os
import openai
from dotenv import load_dotenv

load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

client = openai.OpenAI(
    api_key=deepseek_api_key,
    base_url="https://api.deepseek.com/v1"
)

def deepseek_chat():
    print("DeepSeek对话助手已启动，输入quit/q/exit退出对话")
    while True:
        user_input = input("你：")
        if user_input.lower() in ["quit", "q", "exit"]:
            print("对话结束")
            break

        print("助手：", end="", flush=True)
        stream = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_input}],
            stream=True
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print()
if __name__ == "__main__":
    deepseek_chat()