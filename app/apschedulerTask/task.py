from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from app import app
from app import db
from app.models import User


def show_user():
    with db.app.app_context():
        print(User.query.all())


import random
l = ['a', 'b', 'c', 'd']

c = random.sample(l, 2)


def insert_user():
    with db.app.app_context():
        c = random.sample(l, 2)
        u = User(''.join(c), "test@qq.com")
        db.session.execute(
            'insert into user(username,email) value("{0}","{1}")'.format(
                u.username, u.email))
        print('insert success')


def updateConfig():

    app.config.update(
        JOBS=[
            {
                'id': 'job1',
                'func': show_user,
                'trigger': 'interval',
                'seconds': 2
            },
            {
                'id': 'job2',
                'func': insert_user,
                'trigger': 'interval',
                'seconds': 2
            }
        ],
        SCHEDULER_JOBSTORES={
            'mysql': SQLAlchemyJobStore(
                url=app.config.get('SQLALCHEMY_DATABASE_URI')
            )
        },
        SCHEDULER_API_ENABLED=True
    )
