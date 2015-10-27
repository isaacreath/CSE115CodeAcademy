# import statements
from flask import Blueprint, jsonify, request, redirect
from flask.ext.login import login_required, login_user, logout_user, current_user
from cse115 import db
from cse115.User import User
from werkzeug import check_password_hash, generate_password_hash

auth_blue = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blue.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	user = db.users.find_one({'email': email})

	if user is not None and check_password_hash(user['password_hash'], request.form['password']):
		login_user(User(user['uid']), False)
		return redirect('auth/dashboard')

	else:
		return 'login failed :('


	# pwd_hash = generate_password_hash(request.form['password'])
	
	# return 'login'

@auth_blue.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return 'logout'

@auth_blue.route('/dashboard', methods=['GET'])
def dashboard():
	if current_user.is_authenticated:
		return 'User Id: %s'%(current_user.uid)
	else:
		return 'not logged in'