from pydantic import BaseModel

class UserRegisterValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    city: str

class EditUserValidator(BaseModel):
    count: int
    price: str