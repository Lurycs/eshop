from fastapi import APIRouter
from phone import PhoneAddValidator, PhoneEditValidator
from database.phoneservice import add_phone_db, delete_phone_db, edit_phone_db, check_phone_db, get_exact_phone_db


phone_route = APIRouter(prefix='/phone', tags=['Работа с телефонами'])

# Добавляем телефон
@phone_route.post('/add-phone')
async def add_phone(data: PhoneAddValidator):

    new_phone_data = data.model_dump()

    checker = check_phone_db(data.phone_name)

    if checker == False:
        result = add_phone_db(**new_phone_data)
        return {"message": result}
    else:
        return {'message': 'Такой телефон уже существует'}

# Удаляем телефон
@phone_route.delete('/delete-phone')
async def delete_phone(phone_name: str):
    checker = delete_phone_db(phone_name)

    if checker:
        return checker
    else:
        return {'message': 'Такой телефон не существует'}

@phone_route.put('/edit-phone')
async def edit_phone(data: PhoneEditValidator):

    new_phone_data = data.model_dump()

    checker = check_phone_db(data.phone_name)

    if not checker:
        result = edit_phone_db(**new_phone_data)
        return {"message": result}
    else:
        return {'message': 'Такой телефон уже существует'}

# Информация о телефоне
@phone_route.get('/get-phone')
async def get_phone(phone_name: str):

    exact_phone = get_exact_phone_db(phone_name)
    if exact_phone:
        return exact_phone
    else:
        return {'message': 'Такого телефона не существует'}
