from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a very funny AI assistant."},
        {"role": "user", "content": "Tell me a joke about data scientists."},
    ],
    stream=True,
)
# print(completion.choices[0].message.content)

for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)
