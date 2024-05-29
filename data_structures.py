from sqlalchemy import create_engine, Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import date


Base = declarative_base()
engine = create_engine('sqlite:///language_learning.db')

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True)
    username = Column(String, primary_key=True)
    password = Column(String)
    words_learned_en = Column(Integer, default=0)
    words_learned_fr = Column(Integer, default=0)
    words_learned_it = Column(Integer, default=0)
    info = relationship("UserInfo", back_populates="user", uselist=False)
    notes = relationship("Note", back_populates="user")

class UserInfo(Base):
    __tablename__ = 'user_info'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    email = Column(String)
    date_joined = Column(Date, default=date.today)
    user = relationship("User", back_populates="info")

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    note = Column(String)
    words = Column(String)
    lang = Column(String)
    title = Column(String)
    user = relationship("User", back_populates="notes")

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
    except Exception as e:
        print({e})
    finally:
        close_session(session)  # Make sure the session gets closed no matter
