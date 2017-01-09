from . import app

@app.route('/restpy/v0.1/tasker',methods=['GET'])
def taskList():
    pass


# if __name__ =='__main__':
#     app.run(8888);