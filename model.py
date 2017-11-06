import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    chat_id = Column(Integer, nullable=False)
    questions = relationship('Question', backref='user')


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True)
    chat_id = Column(Integer, nullable=False)
    answers = relationship('Answer', backref='admin')


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    subject = Column(String)
    text = Column(Text)
    answers = relationship('Answer', backref='question')
    questioner_id = Column(Integer, ForeignKey(User.id))


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    text = Column(Text)
    question_id = Column(Integer, ForeignKey(Question.id))
    answerer_id = Column(Integer, ForeignKey(Admin.id))


engine = create_engine('sqlite:///database00.db')
Base.metadata.create_all(engine)
