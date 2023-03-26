from config import TOKEN as API_KEY
import requests

url = "https://api.openai.com/v1/chat/"

prompt = str(input('Введите запрос'))

response = requests.post(
	url,
	headers={
		"Content-Type": "application/json",
		"Authorization": "Bearer {API_KEY}", # замените "API_KEY" на свой ключ API
	},
	json={
		"prompt": prompt,
		"temperature": 0.7,
		"max_tokens": 50,
		"stop": ["\n", "User:"]
	}
)

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])
else:
    print("Произошла ошибка: \n", response.json())

