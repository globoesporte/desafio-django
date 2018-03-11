from enquetes.celery import app

@app.task
def save_db(choice):
    for choice in choices:
       
