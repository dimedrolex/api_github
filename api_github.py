import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'


# Создание вызова API (get запрос)
req_get = requests.get(url)
print("Status code:", req_get.status_code)


# Сохранение ответа API
response_dict = req_get.json()

# Узнаем какие ключи содержит словарь
# print(response_dict.keys())

# Представляет общее количество репозиториев Python GitHub
print("Total repositories:", response_dict['total_count'])

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# Анализ пятого репозитория
repo_dict = repo_dicts[4]
print("Keys:", len(repo_dict))
print("\nSelected information about five repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
