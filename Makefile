runserver:
	python manage.py runserver
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
shell_plus:
	python manage.py shell_plus
flake:
	flake8 .
createuser:
	python manage.py createsuperuser --username admin
