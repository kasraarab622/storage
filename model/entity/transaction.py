import re
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base
from datetime import datetime


class Transaction(Base):
    __tablename__ = "transaction_tbl"

    id = Column(Integer, primary_key=True)
    # person_id = Column(Integer, ForeignKey("person_tbl.id"))
    stuff_id = Column(Integer, ForeignKey("stuff_tbl.id"))
    stuff_count = Column(Integer)
    date_time = Column(DateTime)
    count = Column(Integer)
    type = Column(String(3))
    deleted = Column(Boolean, default=False)

    # person = relationship("Person",back_populates="transaction")
    stuff = relationship("Stuff")

    def __init__(self, id, person_id, stuff_id, date_time, count, type):
        self._id = id
        self._person_id = person_id
        self._stuff_id = stuff_id
        self._date_time = date_time
        self._count = count
        self._type = type

    def __repr__(self):
        return str(self.__dict__)

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        if isinstance(person_id, int) and person_id > 0:
            self._person_id = person_id
        else:
            raise ValueError("Invalid PersonID")

    @property
    def stuuf_id(self):
        return self._stuff_id

    @stuuf_id.setter
    def stuuf_id(self, stuff_id):
        if isinstance(stuff_id, int) and stuff_id > 0:
            self._stuff_id = stuff_id
        else:
            raise ValueError("Invalid StuffID")

    @property
    def datetime(self):
        return self._date_time

    @datetime.setter
    def datetime(self, datetime):
        dt = datetime.strptime(datetime, "%Y-%M-%D %H:%M:%S")
        if ('2025-1-1 00:00:00') > dt > ('2023-1-1 00:00:00'):
            self._date_time = datetime
        else:
            raise ValueError("Invalid Date")

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if isinstance(count, int) and count > 0:
            self._count = count
        else:
            raise ValueError("Invalid Count")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str) and type in ('in,out'):
            self._type = type
        else:
            raise ValueError("Invalid type")
