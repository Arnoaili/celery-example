from celery import Celery

app = Celery('tasks',
              broker='amqp://localhost',
	          backend='amqp://localhost')

# amqp://127.0.0.1:5672

@app.task
def add(x,y):
    print("running...",x,y)
    return x+y

@app.task
def subtract(x,y):
    print('calculating...',x,y)
    return x-y


# celery -A tasks worker --loglevel=info
# celery -A proj worker -l info
