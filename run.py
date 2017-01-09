import os,sys
from views import app

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

app.run(8888)