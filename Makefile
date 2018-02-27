install:
	pip install -r requirements.txt
	python main/manage.py migrate
	python main/manage.py createsuperuser
	python main/manage.py collectstatic

migrations:
	python main/manage.py makemigrations
	python main/manage.py migrate


teste:
	python main/manage.py runserver

run:
	python main/manage.py runserver
