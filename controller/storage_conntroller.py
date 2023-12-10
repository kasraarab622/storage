from model.da.storage_da import *
from model.entity.storage import Storage


class StorageController:
    @classmethod
    def save(cls, stuff_id, count):
        try:
            stuff_da = StuffDa()
            stuff = stuff_da.find_by_id(Stuff, stuff_id)
            stuff_da.session.close()

            da = StorageDa()
            storage = Storage(stuff, count)
            da.save(storage)
            return True, storage
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, stuff_id, count):
        try:
            da = StorageDa()
            storage = da.find_by_id(Storage, id)
            storage.id = id
            storage.stuff_id = stuff_id
            storage.count = count
            da.edit(storage)
            return True, storage
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = StorageDa()
            storage = da.find_by_id(Storage, id)
            da.remove(storage)
            return True, storage
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = StorageDa()
            return da.find_all(Storage)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = StorageDa
            return da.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_stuff_id(cls, stuff_id):
        try:
            da = StorageDa()
            return da.find_by_stuff_id(stuff_id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_count(cls, count):
        try:
            da = StorageDa()
            return da.find_by_count(count)
        except Exception as e:
            return False, str(e)
