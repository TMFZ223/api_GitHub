Инструкция по запуску теста.
Для работы теста у вас должен быть зарегистрирован аккаунт на GITHUB, также у вас должен быть токен, который будет передаваться в заголовках запроса.
Чтобы получить или создать токен API на GitHub, необходимо
1. Войти в свою учётную запись GitHub.
2. Перейти в настройки (Нажать на свою аватарку в правом верхнем углу экрана, в выпадающем меню выбрать "Settings".)
3. Перейти к настройкам разработчика (в меню слева выбрать "Developer settings".)
4. В меню слева выбрать "Personal access tokens" и нажать на "Tokens (classic)" для создания классического токена доступа.
5. Нажать на кнопку "Generate new token" (Создать новый токен).
При создании вам будет предложено ввести описание, выбрать срок действия токена, а также выбрать необходимые разрешения для него.
   - Выберите необходимые разрешения (scopes). Для управления репозиториями выберите repo.
   - Нажмите "Generate token" (Создать токен).
6. скопируйте и сохраните токен.
  
  Файл .env
  В данном файле описаны переменные окружения, которые будут использоваться в запросах на добавление, просмотр и удаление репозитория.
GITHUB_USERNAME=your_user_name
GITHUB_TOKEN=Bearer your_token
REPO_NAME=your_repository_witch_you_want_to_create
В этом файле вам нужно заменить следующие значения на актуальные:
your_user_name, your_token, your_repository_witch_you_want_to_create
В самом коде теста ничего менять не нужно.
В коде теста сначала происходит добавление репозитория (это POST запрос, в заголовках которого передаётся токен авторизации, тело этого запроса в формате JSON), затем проверяется появилось ли поле name в ответе, а также код 201, который отвечает за успешное создание репозитория.
Нам нужно выяснить: появился ли созданный репозиторий у пользователя?
Это мы можем сделать с помощью GET запроса на репозитории пользователя.
После выполнения этого запроса проверяется, есть ли имя созданного ранее репозитория, далее мы удаляем репозиторий с помощью DELETE запроса, в заголовках которого передаём токен авторизации.
Наконец мы проверяем, удалился ли репозиторий, статус код 204 отвечает за то, что удаление было произведено успешно.
Однако это ещё не всё, бывает и так, что серверная логика реализована не верно, появился нужный статус код, а удаления не произошло.
Поэтому в тесте сначала происходит ожидание 20 секунд, так как для удаления нужно какое-то время, а затем ещё раз вызывается функция проверки существования репозиториев, в данном случае проверяется то, что имя репозитория не содержится в списке.
Для запуска теста у вас должны быть установлены следующие библиотеки:
requests, pytest, python-dotenv.
В каталоге есть файл requirements.txt, в котором прописаны библиотеки необходимые для работы теста.
Если что-то у вас не установлено, вы можете в командной строке набрать pip install -r requirements.txt.
Для запуска теста, откройте папку с проектом в командной строке и введите следующее:
python -m pytest test_github_example.py