from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    def __init__(self,username,eamil):
        self.username = username
        self.email = eamil


def show_user():
    with db.app.app_context():
        print(User.query.all())

import random
l = ['a','b','c','d']

c = random.sample(l,2)


def insert_user():
    with db.app.app_context():
        c = random.sample(l,2)
        u = User(''.join(c),"test@qq.com")
        db.session.execute('insert into user(username,email) value("{0}","{1}")'.format(u.username,u.email))
        print('insert success')



if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object('config.DBConfig')

    app.config.update(
        JOBS = [
            {
                'id': 'job1',
                'func': show_user,
                'trigger': 'interval',
                'seconds': 2
            },
            {
                'id':'job2',
                'func':insert_user,
                'trigger':'interval',
                'seconds':2
            }
        ],
        SCHEDULER_JOBSTORES={'mysql': SQLAlchemyJobStore(
            url=app.config.get('SQLALCHEMY_DATABASE_URI'))},
        SCHEDULER_API_ENABLED = True
    )

    db.app = app
    db.init_app(app)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    app.run()
