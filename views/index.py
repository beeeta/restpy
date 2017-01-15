from flask import Flask
app = Flask(__name__)

@app.route('/restpy/v0.1/tasker',methods=['GET'])
def taskList():
    return 'hello'