from celery import Celery

app = Celery('tasks', backend='amqp://celery:123456@localhost/celeryvhost' , broker='amqp://celery:123456@localhost/celeryvhost')

@app.task
def add(x, y):
    return x + y