from fastapi import FastAPI
from user.user_api import user_router
from phone.phone_api import phone_route

app = FastAPI(docs_url='/')

# Создать базу
from database import Base, engine
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(phone_route)

@app.get('/home')
async def home():
    return {'message': 'Hi, this is home page'}
