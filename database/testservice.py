from .models import Result, Questions
from database import get_db

# Добавление вопросов
def add_question_db(main_question, answer1, answer2,
                    answer3=None, answer4=None):
    db = next(get_db())
    if answer3 and answer4:
        new_question = Questions(main_question=main_question, answer1=answer1,
                             answer2=answer2, answer3=answer3, answer4=answer4)
    else:
        new_question = Questions(main_question=main_question, answer1=answer1,
                             answer2=answer2)
    db.add(new_question)
    db.commit()
# выведение топ 5
def get_5_leaders_db():
    db = next(get_db())
    leaders = db.query(Result.user_id).order_by(Result.correct_answers)
    return leaders[:5]
# получение 20 вопросов
def get_questions_db():
    db = next(get_db())
    questions = db.query(Questions).all()
    return questions[:20]
