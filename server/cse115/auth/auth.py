# import statements
from flask import Blueprint

auth_blue = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blue.route('/login', methods=['GET'])
def login():
	return 'login'

@auth_blue.route('/logout', methods=['GET'])
def logout():
	return 'logout'

@auth_blue.route('/dashboard', methods=['GET'])
def dashboard():
	return 'dashboard'