import os


from openai import OpenAI


api_key = os.getenv("DEEPSEEK_API_KEY")


if not api_key:
    raise ValueError("未读取到DEEPSEEK_API_KEY环境变量")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)


response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "system",
            "content": "你是一名面向Python初学者的老师，回答时必须使用生活类比。",
        },
        {
            "role": "user",
            "content": "请用一个生活中的例子解释Python列表，不超过150字。",
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


finish_reason = response.choices[0].finish_reason


print("===== 模型回答 =====")
print(answer)


print("\n===== 响应信息 =====")
print(f"模型：{response.model}")
print(f"结束原因：{finish_reason}")


if response.usage:
    print(f"输入Token: {response.usage.prompt_tokens}")
    print(f"输出Token: {response.usage.completion_tokens}")
    print(f"总Token: {response.usage.total_tokens}")