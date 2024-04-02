from sqlalchemy import (Column, Integer, BigInteger,
                        String, ForeignKey, Float, Date, DateTime, Boolean)
from sqlalchemy.orm import relationship
from database import Base
class Users(Base):
    # даем название таблице
    __tablename__ = "users"
    # создаем колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    level = Column(String, default="Easy")
    phone_number = Column(String, unique=True)
    datetime = Column(DateTime)
class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, unique=True, nullable=False)
    answer1 = Column(String)
    answer2 = Column(String)
    answer3 = Column(String, nullable=True)
    answer4 = Column(String, nullable=True)
    correct_answer = Column(Integer, nullable=False)

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String)
    # создаем связь с другой таблицей
    user_fk = relationship(Users, foreign_keys=[user_id],
                           lazy="subquery")
class UserAnswers(Base):
    __tablename__ = "user_answers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    q_id = Column(Integer, ForeignKey("questions.id"))
    level = Column(String, ForeignKey("users.level"))
    user_answer = Column(Integer)
    correctness = Column(Boolean, default=False)
    timer = Column(DateTime)

    user_fk = relationship(Users, foreign_keys=[user_id],
                           lazy="subquery")
    question_fk = relationship(Questions, foreign_keys=[q_id],
                               lazy="subquery")

