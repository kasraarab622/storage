from model.da.stuffgroup_da import StuffGroupDa
from model.entity.stuff_group import StuffGroup

class StuffGroupController:
    @classmethod
    def save(cls, title, parent_id):
        try:
            stuffgroup = StuffGroupDa(title,parent_id)
            stuffgroup.title = title
            stuffgroup.parent_id = parent_id
            da = StuffGroupDa()
            da.save(stuffgroup)
            return True, stuffgroup
        except Exception as e:
            return False,str(e)

    @classmethod
    def edit(cls, id, title, parent_id):
        try:
            da = StuffGroupDa()
            stuffGroup = da.find_by_id(StuffGroup,id)
            stuffGroup.id = id
            stuffGroup.title = title
            stuffGroup.parent_id = parent_id
            da.edit(stuffGroup)
            return True, stuffGroup
        except Exception as e:
            return False,str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = StuffGroupDa()
            stuffGroup = da.find_by_id(StuffGroup,id)
            da.remove(id)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = StuffGroupDa
            return da.find_all(StuffGroup)
        except Exception as e:
            return False,str(e)
    @classmethod
    def find_by_id(cls, id):
        try:
            da = StuffGroupDa()
            return da.find_by_id(StuffGroup,id)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_title(cls, title):
        try:
            da = StuffGroupDa()
            return da.find_by_title(StuffGroup,title)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_parent_id(cls, parent_id):
        try:
            da = StuffGroupDa()
            return da.find_by_perent_id(StuffGroup,parent_id)
        except Exception as e:
            return False,str(e)
