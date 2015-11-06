from flask import Blueprint, jsonify, request
from flask.ext.login import login_required, current_user
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

	# fill out users assignments
	assignments = {}
	num_assignments = db.assignments.count()

	for i in range(1, num_assignments + 1)
		assignment_dict = {}
		db_assignment = db.assignments.find({'num': 1})
		starter_code = db_assignment['starter_code']
		assignment_dict['completion'] = 'not started'
		assignment_dict['starter_code'] = starter_code
		assignment{i : assignment_dict}

	user['assignments'] = assignments

	# get users id number
	id_dict = db.counter.find_one({'id_count':{'$gt': 999}})
	uid = id_dict['id_count']
	user['uid'] = uid
	db.counter.update({'id_count': {'$gt': 999}}, {'id_count': uid + 1})

	# add user to db.user
	db.users.insert(user)
	return 'Success!'

@user_blue.route('/get_assignments', methods=['GET'])
def get_assignments():
	uid = current_user.uid
	user = db.users.find_one({'uid': uid})
	num_assignments = db.assignments.count()

	# assignments = db.assignments.find({})

	output = {}
	records = []

	for i in range(1, num_assignments + 1):
		# do something
		assignment_doc = {}
		assignment = db.assignments.find_one({'number': i})

		assignment_doc['assignment'] = 'Assignment %s'%(i)
		assignment_doc['description'] = assignment['title']
		assignment_doc['completion'] = user['assignments']['%s'%(i)]['completion']
		records.append(assignment_doc)

	output['records'] = records	
	return jsonify(output)

