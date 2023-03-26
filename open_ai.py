import openai
from config import API_KEY

openai.api_key = API_KEY

prompt = str(input('Введите запрос: '))
model = "text-davinci-002"

response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50,
    temperature=0.7,
    n=1,
    stop=None,
)

print(response.choices[0].text)
