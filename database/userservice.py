from database.models import (Users, UserAnswers,
                             Questions, Result)
from datetime import datetime
from database import get_db

# регистрация пользователя
def register_user_db(username, phone_number, level):
    db = next(get_db())
    checker = db.query(Users).filter_by(phone_number=phone_number).first()
    if checker:
        return checker.id
    else:
        new_user = Users(username=username, phone_number=phone_number,
                         level=level, datetime=datetime.now())
        db.add(new_user)
        db.commit()
        return new_user
# принимаем ответы пользователя
def user_answer_db(user_id, q_id, level, user_answer):
    db = next(get_db())
    exact_question = db.query(Questions).filter_by(id=q_id).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False
        new_answer = UserAnswers(user_id=user_id, q_id=q_id,
                                 user_answer=user_answer, level=level,
                                 correctness=correctness,
                                 timer=datetime.now())
        db.add(new_answer)
        db.commit()
    all_leaders = (db.query(Result.user_id).
                   order_by(Result.correct_answers))
    return all_leaders.index((user_id, )) + 1
# суммация баллов
def plus_point_user_db(user_id, correct_answer):
    db = next(get_db())
    checker = db.query(Result).filter_by(user_id=user_id).first()
    if checker:
        checker.correct_answers += correct_answer
    else:
        new_leader_data = Result(user_id=user_id, correct_answers=correct_answer)
        db.add(new_leader_data)
        db.commit()

        # получение позицию в списке
        all_leaders = (db.query(Result.user_id).
                       order_by(Result.correct_answers))
        return all_leaders.index((user_id,)) + 1
# получение всех юзеров
def get_all_users_db():
    db = next(get_db())
    users = db.query(Users).all()
    return users