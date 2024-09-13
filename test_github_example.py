import os
import requests
import time
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
# Заголовок в запросе
headers_in_the_request = {"Authorization": f"{GITHUB_TOKEN}"}
# Данные тела запроса
payload = {"name": f"{REPO_NAME}", "private": False}
class Test_git_apy:
    # Функция создания репозя для использования в тесте
    def create_repository(self):
        response = requests.post('https://api.github.com/user/repos', headers = headers_in_the_request, json = payload) # Создаём репозиторий в своём аккаунте
        response_dict = response.json()
        return response, response_dict
    # Функция проверки существования запроса для использования в тесте
    def repository_exists(self):
        response = requests.get(f'https://api.github.com/users/{GITHUB_USERNAME}/repos') # получение репозиториев пользователя
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]
        return repo_names
    # Функция удаления репозитория для использования в тесте
    def delete_repository(self):
        response = requests.delete(f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}', headers = headers_in_the_request)
        return response
    def test_working_with_git_repository(self):
        # Создание репозитория
        response, response_dict = self.create_repository()
        assert "name" in response_dict, "There is no field 'name' in the response" # Проверяем поле имени в создавшемся репозитории
        assert response.status_code == 201, "problems with creating repository" # успешное создание репозитория, в противном случае при создании возникли проблемы
        # Проверка существования репозитория
        repo_names = self.repository_exists()
        assert REPO_NAME in repo_names, "repository not found in this list"
        # Удаление репозитория
        response = self.delete_repository()
        assert response.status_code== 204 , "problems with deleting repository"
        # Ждём 20 секунд, чтобы удалились все данные, связанные с репозиторием
        time.sleep(20)
        # Вызываем повторно функцию существования репозитория, чтобы убедиться в его успешном удалении
        repo_names = self.repository_exists()
        assert REPO_NAME not in repo_names, "repository exists in this list"