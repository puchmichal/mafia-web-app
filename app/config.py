import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mafia_will_get_you'
    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_ONYX_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False