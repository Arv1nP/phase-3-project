from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class User:
    def __init__(self, username):
        self.username = username
        # Other user attributes and methods
