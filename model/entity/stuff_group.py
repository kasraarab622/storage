import re
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Null
from sqlalchemy.orm import relationship

from model.entity import *
class StuffGroup(Base):
    __tablename__ = "stuff_group_tbl"

    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    parent_id = Column(Integer, ForeignKey("stuff_group_tbl.id"), nullable=True)
    deleted = Column(Boolean, default=False)

    parent = relationship('StuffGroup')

    def __init__(self, title,parent=None):
        self.title = title
        if parent:
            self.parent_id = parent.id
    #
    # @property
    # def title(self):
    #     return self._title
    #
    # @title.setter
    # def title(self, title):
    #     if isinstance(title, str) and re.match(r"^[a-zA-Z\s]{3,20}", title):
    #         self._title = title
    #     else:
    #         raise ValueError("Invalid Title")
    # @property
    # def parent_id(self):
    #     return self._parent_id
    # @parent_id.setter
    # def parent_id(self, parent_id):
    #     if isinstance(parent_id, int) and parent_id >= 1:
    #         self._parent_id = parent_id
    #     else:
    #         raise ValueError("Invalid ParentID")
