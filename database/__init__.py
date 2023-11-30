from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Мы тут показываем ссылку в БД
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/eshop1'
# Подключаемся к нашему базе
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Импорт всех моделей
from database import models

# Генератор соединений в БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()

