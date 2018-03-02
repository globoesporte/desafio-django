#!/bin/sh


#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

export BROKER_URL=amqp://admin:mypass@rabbit//

# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
su -m myuser -c "celery worker -A home_site -l info " &


# wait Celery to start
sleep 5

# prepare init migration
python3 manage.py makemigrations home_site
# migrate db, so we have the latest db schema
python3 manage.py migrate
# start development server on public ip interface, on port 8000
python3 manage.py runserver 0.0.0.0:8000 