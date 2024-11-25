install:
	poetry install
	poetry lock --no-update
migrate:
	poetry run python manage.py makemigrations
build:
	./build.sh
	make migrate
start:
	poetry run python manage.py runserver
lint:
	poetry run flake8 task_manager --exclude=migrations