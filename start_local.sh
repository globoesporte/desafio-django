# !/bin/sh

celery -A home_site worker -l info &
python3 manage.py runserver  0.0.0.0:8000