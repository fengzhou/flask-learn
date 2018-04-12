from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore



class Config(object):
    DEBUT = True




class DBConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:fengzhou@127.0.0.1:3306/gitlearn'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True