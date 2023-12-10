import re
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from model.entity import *

class Person(Base):
    __tablename__ = "person_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    family = Column(String(20))
    phone_number = Column(String(11))
    email = Column(String(50))
    username = Column(String(20))
    password = Column(String(10))
    active = Column(Boolean,default=True)
    deleted = Column(Boolean, default=False)

    transaction = relationship("Transaction",back_populates="person")

    def __init__(self, name, family, phone_number, email, username, password, active=True):
        self.name = name
        self.family = family
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.active = active
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,20}$", name):
    #         self._name = name
    #     else:
    #         raise ValueError("Invalid Name")
    #
    # @property
    # def family(self):
    #     return self._family
    #
    # @family.setter
    # def family(self, family):
    #     if isinstance(family, str) and re.match(r"^[a-zA-Z\s]{4,20}$", family):
    #         self._family = family
    #     else:
    #         raise ValueError("Invalid Family")
    #
    # @property
    # def phone_number(self):
    #     return self._phone_number
    #
    # @phone_number.setter
    # def phone_number(self, phone_number):
    #     if isinstance(phone_number, str) and re.match(r"^09\d{9}$", phone_number):
    #         self._phone_number = phone_number
    #     else:
    #         raise ValueError("Invalid PhonNumber")
    #
    # @property
    # def email(self):
    #     return self._email
    #
    # @email.setter
    # def email(self, email):
    #     if isinstance(email, str) and re.match(r"^[\w\.]{5,50}@(gmail|yahoo).com", email):
    #         self._email = email
    #     else:
    #         raise ValueError("Invalid Email")
    #
    # @property
    # def username(self):
    #     return self._username
    #
    # @username.setter
    # def username(self, username):
    #     if isinstance(username, str) and re.match(r"^[\w\.]{5,20}", username):
    #         self._username = username
    #     else:
    #         raise ValueError("Invalid UserName")
    #
    # @property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, password):
    #     if isinstance(password, str) and re.match(r"^[\w\\\*\.\s]{5,10}", password):
    #         self._password = password
    #     else:
    #         raise ValueError("Invalid Password")
    #
    # @property
    # def active(self):
    #     return self._active
    #
    # @active.setter
    # def active(self, active):
    #     self._active = active
