from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL
from datetime import datetime

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    session = Session(engine)
    return session

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    nick_name = Column(String)

class AuthToken(Base):
    __tablename__ = "auth_tokens"
    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


