from database import get_db
from .models import Phone
from datetime import datetime

# Добавляем телефоны
def add_phone_db(phone_name, which_year, phone_color, count, price):

    db = next(get_db())

    new_phone = db.query(Phone).filter_by(phone_name=phone_name, which_year=which_year, phone_color=phone_color,
                                          count=count, price=price)

    db.add(new_phone)
    db.commit()

    return 'Телефоны успешно добавлены '

# Изминения телефона
def edit_phone_db(phone_id, edit_type, new_data):
    db = next(get_db())

    edit_phone = db.query(Phone).filter_by(phone_id=phone_id).first()

    if edit_phone:

        if edit_type == 'count':
            edit_phone.count = new_data
        elif edit_type == 'price':
            edit_phone.price = new_data

        db.commit()

        return 'Телефон успешно изменен '
    else:
        return 'Такого телефона нет'

#Удаления телефона из БД
def delete_phone_db(phone_id):
    db = next(get_db())

    delete_phone = db.query(Phone).filter_by(phone_id=phone_id).first()

    if delete_phone:
        db.delete(delete_phone)
        db.commit()
        return 'Телефон успешно удален'
    else:
        return 'Такого телефона нет'

def check_phone_db(phone_name):
    db = next(get_db())
    try:
        checker = db.query(Phone).filter_by(phone_name=phone_name).one()

        if checker:
            return checker
    except:
        return False


def get_exact_phone_db(phone_name):

    db = next(get_db())

    exact_phones = db.query(Phone).filter_by(phone_name=phone_name).first()

    return f'Телефоны: {exact_phones}'