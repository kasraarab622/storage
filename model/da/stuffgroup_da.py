from model.entity import *
from model.da import *


class StuffGroupDa(DataBaseManager):
    def find_by_title(self, titel):
        self.make_engine()
        result = self.session.query(StuffGroup).filter(StuffGroup.title.like(titel))
        self.session.close()
        return result

    def find_by_perent_id(self, parent_id):
        self.make_engine()
        result = self.session.query(StuffGroup).filter(StuffGroup.parent_id == parent_id)
        self.session.close()
        return result
