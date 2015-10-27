from flask import Flask

app = Flask(__name__)

from cse115.auth.auth import auth_blue
from cse115.user.user import user_blue

app.register_blueprint(auth_blue)
app.register_blueprint(user_blue)
