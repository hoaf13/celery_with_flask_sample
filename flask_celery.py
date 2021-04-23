from flask import Flask
from celery_task import make_celery
import time 

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)

@celery.task(name='flask_celery')
def reverse(name):
    delay = 5
    print(type(celery))
    print("{}: sleep in {} seconds".format(celery, delay))
    time.sleep(delay)
    return name[::-1]

@flask_app.route('/process/<name>')
def process(name):
    a = reverse.delay(name) 
    print("id:", a)
    return "i sent async request!"

if __name__ == '__main__':
    flask_app.run(debug=True)

