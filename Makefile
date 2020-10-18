migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
runserver:
	python manage.py runserver
activatenv:
	source ./env/bin/activate
configure:
	export DJANGO_SETTINGS_MODULE=cursodjango.settings
shellplus:
	python manage.py shell_plus
tests:
	python manage.py test web