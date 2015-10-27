from flask import Blueprint
from cse115 import db

user_blue = Blueprint('user', __name__, url_prefix='/user')

@user_blue.route('/something', methods=['GET'])
def something():
	return 'something'