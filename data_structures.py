from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()
engine = create_engine('sqlite:///language_learning.db')

class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String)
    words_learned_en = Column(Integer, default=0)
    words_learned_fr = Column(Integer, default=0)
    words_learned_it = Column(Integer, default=0)

def create_session(engine):
    """Create and return a new session"""
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def close_session(session):
    """Close the provided session"""
    try:
        session.close()
    except Exception as e:
        print(f"Error closing session: {e}")

if __name__ == "__main__":
    try:
        DATABASE_URL = 'sqlite:///language_learning.db'
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = create_session(engine)
        # Do something with the session
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_session(session)  # Make sure to close the session even if an exception occurs
