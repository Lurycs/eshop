from .models import User
from database import get_db
from datetime import datetime


# Регистрация пользователя
def register_user_db(name, surname, phone_number, email, city, password):
    db = next(get_db())

    new_user = db.query(User).filter_by(name=name, surname=surname, phone_number=phone_number,
                                        email=email, city=city, password=password, reg_dat=datetime.now())

    db.add(new_user)
    db.commit()

    return 'Пользователь успешно добавлен!)'

# Информацтя о рользователе
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return f'Пользователи: {exact_user}'

# Изменить пльзователя
def edit_user_db(user_id, edit_type, new_data  ):

    db = next(get_db())

    new_user = db.query(User).filter_by(user_id=user_id).first()

    if new_user:
        if edit_type == 'password':
            new_user.password = new_data
        elif edit_type == 'email':
            new_user.email = new_data
        elif edit_type == 'phone_number':
            new_user.phone_number = new_data
        elif edit_type == 'city':
            new_user.city = new_data

        db.commit()

        return 'Данные успешно изменины'
    else:
        return 'Пользователь не найден'

# Удаления пользователя
def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        db.delete(delete_user)
        db.commit()

        return 'Пользователь успешно удален'
    else:
        return 'Пользователь не найден'

def check_user_email_db(email):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return checker
    else:
        return 'Такого email нету'
