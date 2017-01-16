import sys,os
sys.path.append(os.path.abspath(os.path.pardir))
from restpy import db,app

with app.app_context():
    db.create_all()
