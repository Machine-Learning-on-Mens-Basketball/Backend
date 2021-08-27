import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DATABASE_USER = os.getenv('DATABASE_USER', 'db_user_id')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'db_user_password')
    DEBUG = False