from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True)
    company_id = db.Columm(db.Integer,db.ForeignKey('company.id'))
    company = db.relationship('Company',backref=db.backref('user',lazy='dynamic'))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r,%r,%r>' % self.username,self.password,self.email

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Company %r>' % self.name
