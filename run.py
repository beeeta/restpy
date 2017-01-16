import os,sys
from views.index import app

# sys.path.append(os.path.dirname(os.path.realpath(__file__)))

app.run(host='0.0.0.0',port=8888)