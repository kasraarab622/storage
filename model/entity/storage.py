from model.entity.base import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Storage(Base):
    __tablename__ = "storage_tbl"

    id = Column(Integer, primary_key=True)
    stuff_id = Column(Integer, ForeignKey('stuff_tbl.id'))
    count = Column(Integer)
    deleted = Column(Boolean, default=False)

    stuff = relationship("Stuff",back_populates="storage")

    def __init__(self, stuff_id, count):
        self.stuff_id = stuff_id
        self.count = count

    # def __repr__(self):
    #     return str(self.__dict__)
    #
    # @property
    # def stuff_id(self):
    #     return self._stuff_id
    #
    # @stuff_id.setter
    # def stuff_id(self, stuff_id):
    #     if isinstance(stuff_id, int) and stuff_id > 0:
    #         self._stuff_id = stuff_id
    #     else:
    #         raise ValueError("Invalid StuffID")
    #
    # @property
    # def count(self):
    #     return self._count
    #
    # @count.setter
    # def count(self, count):
    #     if isinstance(count, int) and count > 0:
    #         self._count = count
    #     else:
    #         raise ValueError("Invalid Count")
