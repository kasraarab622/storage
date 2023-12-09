from model.da.stuff_da import StuffDa
from model.entity.stuff import Stuff


class StuffController:
    @classmethod
    def save(cls, name, brand, description, groupid):
        try:
            stuff = Stuff()
            stuff.name = name
            stuff.brand = brand
            stuff.description = description
            stuff.groupid = groupid
            da = StuffDa()
            da.save(Stuff)
            return True, Stuff
        except Exception as e:
            return e

    @classmethod
    def edit(cls, id, name, brand, description, groupid):
        try:
            da = StuffDa()
            Stuff = da.find_by_id(id)
            Stuff.name = name
            Stuff.brand = brand
            Stuff.description = description
            Stuff.groupid = groupid
            da.edit(Stuff)
            return True, Stuff
        except Exception as e:
            return e

    @classmethod
    def remove(cls, id):
        try:
            da = StuffDa()
            Stuff = da.find_by_id(id)
            da.remove(id)
            return True, id
        except Exception as e:
            return e

    @classmethod
    def find_all(cls):
        try:
            da = StuffDa()
            return da.find_all(Stuff)
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            da = StuffDa()
            return da.find_by_id(id)
        except Exception as e:
            return e

    @classmethod
    def find_by_name(cls, name):
        try:
            da = StuffDa()
            return da.find_by_name(name)
        except Exception as e:
            return e

    @classmethod
    def find_by_brand(cls, brand):
        try:
            da = StuffDa()
            return da.find_by_brand(brand)
        except Exception as e:
            return e

    @classmethod
    def find_by_description(cls, description):
        try:
            da = StuffDa()
            return da.find_by_description(description)
        except Exception as e:
            return e

    @classmethod
    def find_by_groupid(cls, groupid):
        try:
            da = StuffDa()
            return da.find_by_groupid(groupid)
        except Exception as e:
            return e
