from model.da.stuffgroup_da import StuffGroupDa
from model.entity.stuff_group import StuffGroup


class StuffGroupController:
    @classmethod
    def save(cls, title, parent_id):
        try:
            stuffgroup = StuffGroupDa()
            stuffgroup.title = title
            stuffgroup.parent_id = parent_id
            da = StuffGroupDa()
            da.save(StuffGroup)
            return True, stuffgroup
        except Exception as e:
            e.with_traceback()
            return e

    @classmethod
    def edit(cls, id, title, parent_id):
        try:
            da = StuffGroupDa()
            StuffGroup = da.find_by_id(id)
            StuffGroup.id = id
            StuffGroup.title = title
            StuffGroup.parent_id = parent_id
            da.edit(StuffGroup)
            return True, StuffGroup
        except Exception as e:
            return e

    @classmethod
    def remove(cls, id):
        try:
            da = StuffGroupDa()
            StuffGroup = da.find_by_id(id)
            da.remove(StuffGroup)
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            da = StuffGroupDa()
            return da.find_by_id(StuffGroup, id)
        except Exception as e:
            return e

    @classmethod
    def find_by_title(cls, title):
        try:
            da = StuffGroupDa()
            return da.find_by_title(StuffGroup, title)
        except Exception as e:
            return e

    @classmethod
    def find_by_parent_id(cls, parent_id):
        try:
            da = StuffGroupDa()
            return da.find_by_perent_id(StuffGroup, parent_id)
        except Exception as e:
            return e
