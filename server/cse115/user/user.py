from flask import Blueprint, jsonify, request
from cse115 import db
from werkzeug import generate_password_hash

user_blue = Blueprint('user', __name__, url_prefix='/user')

@user_blue.route('/add_user', methods=['GET', 'POST'])
def add_user():
	user = {}
	#check if email is already in use
	if db.users.find_one({'email' : request.form['email'] }):
		return 'email in use :('
	
	user['email'] = request.form['email']

	# generate users password hash
	user['password_hash'] = generate_password_hash(request.form['password'])

	# get users id number
	id_dict = db.counter.find_one({'id_count':{'$gt': 999}})
	uid = id_dict['id_count']
	user['uid'] = uid
	db.counter.update({'id_count': {'$gt': 999}}, {'id_count': uid + 1})

	# add user to db.user
	db.users.insert(user)
	return 'Success!'
