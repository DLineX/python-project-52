### Hexlet tests and linter status:
[![Actions Status](https://github.com/DLineX/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DLineX/python-project-52/actions)
[![Github Actions Status](https://github.com/DLineX/python-project-83/workflows/Github%20Actions/badge.svg)](https://github.com/DLineX/python-project-83/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/9dd930753f9b2b54ea1e/maintainability)](https://codeclimate.com/github/DLineX/python-project-52/maintainability)
### Task Manager:

#### (ENG) A simple and flexible task management web application

#### (RU) Простое веб-приложение для менеджмента задач

### Описание:
#### Task Manager – система управления задачами. Она позволяет ставить задачи, добавлять метки на них, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация
### Технологический стек:
#### * [Python 3.10](https://www.python.org/doc/)
#### * [Django 5.1.2](https://docs.djangoproject.com/en/5.1/)
#### * [Bootstrap5 24.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
#### * [Poetry 1.8.3](https://python-poetry.org/docs/)

### Установка и запуск приложения 
1. Склонировать репозиторий командой:
``` git clone https://github.com/DLineX/python-project-52.git ```
2. В корень проекта добавить файл ```.env``` с переменными DATABASE_URL и SECRET_KEY
```
DATABASE_URL = path/to/database
SECRET_KEY = database_password
```
	
3. В директории проекта выполнить команду:
```
make build
```

4. Для запуска приложения выполните команду:
```
 make start
```
