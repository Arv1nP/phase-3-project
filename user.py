from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
