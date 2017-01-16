from flask import make_response,jsonify
from flask_httpauth import HTTPBasicAuth

from .. import app

auth = HTTPBasicAuth()

@app.route('/restpy/v0.1/tasker',methods=['GET'])
@auth.login_required
def taskList():
    return jsonify({'msg':'hello'})

@auth.get_password
def getUser(username):
    if username=='allen':
        return 'bbq'
    return None

@auth.error_handler
def handlerUnauthor():
    return make_response(jsonify({'msg':'author error'}),404)