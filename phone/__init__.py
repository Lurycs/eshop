from pydantic import BaseModel


class PhoneAddValidator(BaseModel):
    phone_name: str
    which_year: int
    phone_color: str
    count: int
    price: str


class PhoneEditValidator(BaseModel):
    phone_name: str
    which_year: int
    phone_color: str
    count: int
    price: str
