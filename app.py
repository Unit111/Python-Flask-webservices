from flask import Flask
from flask_httpauth import HTTPBasicAuth
import os
# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


auth = HTTPBasicAuth()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
    


import handlers
import tasks_routes
import users_routes
import models








