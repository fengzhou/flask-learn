from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler


app = Flask(__name__)
app.config.from_object('config.DBConfig')

db = SQLAlchemy(app)

apscheduler = APScheduler()


from app.apschedulerTask import task

task.updateConfig()

apscheduler.init_app(app)

apscheduler.start()



from .views import *