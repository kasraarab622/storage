# ehtemam
from model.da.database import DataBaseManager
from model.entity.stuff import Stuff


class StuffDa(DataBaseManager):

    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.name.like(name))
        self.session.close()
        return result

    def find_by_brand(self, brand):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.brand.like(brand))
        self.session.close()
        return result

    def find_by_description(self, description):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.description.like(description))
        self.session.close()
        return result

    def find_by_groupid(self, groupid):
        self.make_engine()
        result = self.session.query(Stuff).filter(Stuff.groupid == groupid)
        self.session.close()
        return result
