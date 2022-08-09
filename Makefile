freeze:
	python3 pip freeze > requirements.txt

migrate:
	python3 src/api/manage.py makemigrations
	python3 src/api/manage.py migrate

venv:
	venv/Scripts/activate