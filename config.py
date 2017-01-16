class Config(object):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:../database.db'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dbinit.db'