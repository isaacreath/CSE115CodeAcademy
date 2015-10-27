from flask import Flask
from flask.ext.login import LoginManager
from pymongo import MongoClient
from User import User

client = MongoClient()
db = client.cse115

app = Flask(__name__)

app.config.from_object('config')

# Sessions Stuff
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  return User(user_id)

import logging
file_handler = logging.FileHandler('flask_errors.log')
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

from cse115.auth.auth import auth_blue
from cse115.user.user import user_blue

app.register_blueprint(auth_blue)
app.register_blueprint(user_blue)

if (db.counter.count() == 0):
	db.counter.insert({"id_count" : 1000})
