import os

class Config(object):
    session.secret_key = os.urandom(24) # or "acetate"
