# import statements
from flask import Blueprint
from cse115 import db

auth_blue = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blue.route('/login', methods=['GET'])
def login():
	db.users.insert({'name': 'test',
					 'password_hash': 'asdfhashlk',
					 'uid': 1000})
	return 'login'

@auth_blue.route('/logout', methods=['GET'])
def logout():
	return 'logout'

@auth_blue.route('/dashboard', methods=['GET'])
def dashboard():
	return 'dashboard'