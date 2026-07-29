import os


from openai import OpenAI


api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("未读取到DEEPSEEK_API_KEY环境变量")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)


def ask_ai(question):
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "你是一名面向Python初学者的老师，请使用简单清楚的语言回答。",
            },
            {
                "role": "user",
                "content": question,
            },
        ],
        stream=False,
        extra_body={
            "thinking": {
                "type": "disabled",
            }
        },
    )
    answer = response.choices[0].message.content
    return answer


def main():
    print("===== AI 学习助手 v0.1 =====")
    print("输入 quit 可以退出程序。\n")
    while True:
        question = input("你：").strip()
        if question.lower() == "quit":
            print("程序已退出，再见！")
            break
        if not question:
            print("问题不能为空，请重新输入。\n")
            continue
        try:
            answer = ask_ai(question)
        except Exception as error:
            print("\n请求失败，请检查网络、API Key 或账户余额。")
            print(f"错误信息：{error}\n")
            continue
        print("\nAI：")
        print(answer)

if __name__ == '__main__':
    main()