import re
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from model.entity import *


class Stuff(Base):
    __tablename__ = "stuff_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    brand = Column(String(20))
    group_id = Column(Integer, ForeignKey("stuff_group_tbl.id"))
    description = Column(String(200))
    deleted = Column(Boolean, default=False)

    storage = relationship("Storage", back_populates="stuff")
    stuff_group = relationship("StuffGroup")
    # transaction = relationship("Transaction")

    def __init__(self, name, brand, description, stuff_group):
        self.name = name
        self.brand = brand
        self.description = description
        self.stuff_group = stuff_group
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
    # def brand(self):
    #     return self._brand
    #
    # @brand.setter
    # def brand(self, brand):
    #     if isinstance(brand, str) and re.match(r"^[a-zA-Z\s]{3,20}$", brand):
    #         self._brand = brand
    #     else:
    #         raise ValueError("Invalid Brand")
    #
    # @property
    # def description(self):
    #     return self._description
    #
    # @description.setter
    # def description(self, description):
    #     if isinstance(description, str) and re.match(r"^[\w\.\s]{10,200}$", description):
    #         self._description = description
    #     raise ValueError("Invalid Description")
    #
    # @property
    # def groupid(self):
    #     return self._groupid
    #
    # @groupid.setter
    # def groupid(self, groupid):
    #     if isinstance(groupid, int) and groupid > 0:
    #         self._groupid = groupid
    #     else:
    #         raise ValueError("Invalid GroupID")
