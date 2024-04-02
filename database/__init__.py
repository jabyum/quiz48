from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# подключение/создание базы данных
SQL_ALCHEMY_DATABASE_URI = "sqlite:///data.db"
# создание движка
engine = create_engine(SQL_ALCHEMY_DATABASE_URI)
# команда для создания сессии
SessionLocal = sessionmaker(bind=engine)
# object-relational mapping -ORM
Base = declarative_base()
# создание логики для создания сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
