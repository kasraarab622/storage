from model.da.stuff_da import *
from model.entity.stuff import Stuff


class StuffController:
    @classmethod
    def save(cls, name, brand, description, group_id):
        try:
            group_da = StuffGroupDa()
            group = group_da.find_by_id(StuffGroup,group_id )
            group_da.session.close()

            da = StuffDa()
            stuff = Stuff(name,brand,description,group)
            da.save(stuff)
            return True, stuff
        except Exception as e:
            return False,str(e)

    @classmethod
    def edit(cls, id, name, brand, description, groupid):
        try:
            da = StuffDa()
            stuff = da.find_by_id(Stuff,id)
            stuff.name = name
            stuff.brand = brand
            stuff.description = description
            stuff.groupid = groupid
            da.edit(stuff)
            return True, stuff
        except Exception as e:
            return False,str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = StuffDa()
            stuff = da.find_by_id(Stuff,id)
            da.remove(stuff)
            return True, stuff
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = StuffDa()
            return da.find_all(Stuff)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = StuffDa()
            return da.find_by_id(Stuff,id)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = StuffDa()
            return da.find_by_name(name)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_brand(cls, brand):
        try:
            da = StuffDa()
            return da.find_by_brand(brand)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_description(cls, description):
        try:
            da = StuffDa()
            return da.find_by_description(description)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_groupid(cls, groupid):
        try:
            da = StuffDa()
            return da.find_by_groupid(groupid)
        except Exception as e:
            return False,str(e)
