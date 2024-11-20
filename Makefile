install:
	poetry install
migrate:
	poetry run python manage.py makemigrations
build:
	make install
	make migrate
start:
	poetry run python manage.py runserver
lint:
	poetry run flake8 task_manager