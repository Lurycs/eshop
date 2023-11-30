from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    city = Column(String, nullable=False)
    reg_dat = Column(DateTime)


class Phone(Base):
    __tablename__ = 'phones'
    phone_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    phone_name = Column(String)
    which_year = Column(Integer)
    phone_color = Column(String)
    count = Column(Integer, nullable=False)
    price = Column(String, nullable=False)
    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
