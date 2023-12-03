import re
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from model.entity.base import Base


class Stuff(Base):
    __tablename__ = "stuff_tbl"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    brand = Column(String(20))
    description = Column(String(200))
    groupid = Column(Integer)
    deleted = Column(Boolean, default=False)

    storage = relationship("Storage")

    def __init__(self, name, brand, description, groupid):
        self.name = name
        self.brand = brand
        self.description = description
        self.groupid = groupid

    def __repr__(self):
        return str(self.__dict__)
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
    #     if isinstance(description, str) and re.match("[\w\.\s]{10,200}", description):
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
