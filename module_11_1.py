import requests


url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)


if response.status_code == 200:
  print("Запрос успешен!")
else:
  print(f"Ошибка: {response.status_code}")


data = response.json()
print(f"Полученные данные: {data}")



try:
  response = requests.get("https://nonexistentwebsite.com")
  response.raise_for_status() 
  print(response.text)
except requests.exceptions.RequestException as e:
  print(f"Произошла ошибка при запросе: {e}")
