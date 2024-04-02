from fastapi import APIRouter
from database.userservice import (register_user_db, user_answer_db,
                                  plus_point_user_db, get_all_users_db)
from database.testservice import get_questions_db, add_question_db

user_router = APIRouter(prefix="/user", tags=["users api"])

#регистрация
@user_router.post("/registration")
async def register(username: str, phone_number: str, level: str):
    register = register_user_db(username=username, phone_number=phone_number, level=level)
    return f"{username}, Вы успешно зарегистрировались"
# получение всех юзеров
@user_router.get("/all_users")
async def all_users():
    return get_all_users_db()
@user_router.post("/done")
async def done(user_id: int, correct_answers: int):
    done = plus_point_user_db(user_id, correct_answers)
    return f"Результат {done}"
