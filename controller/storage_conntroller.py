from model.da.storage_da import StorageDa
from model.entity.storage import Storage


class StorageController:
    @classmethod
    def save(cls, stuff_id, count):
        try:
            stronge = Storage()
            stronge.stuff_id = stuff_id
            stronge.count = count
            da = StorageDa()
            da.save(Storage)
            return True, Storage
        except Exception as e:
            return e

    @classmethod
    def edit(cls, id, stuff_id, count):
        try:
            da = StorageDa()
            Storage = da.find_by_id(id)
            Storage.id = id
            Storage.stuff_id = stuff_id
            Storage.count = count
            da.edit(Storage)
            return True, Storage
        except Exception as e:
            return e

    @classmethod
    def remove(cls, id):
        try:
            da = StorageDa()
            Storage = da.find_by_id(id)
            da.remove(id)
            return True, id
        except Exception as e:
            return e

    @classmethod
    def find_all(cls):
        try:
            da =StorageDa()
            return da.find_all(Storage)
        except Exception as e:
            return e
    @classmethod
    def find_by_id(cls, id):
        try:
            da = StorageDa
            return da.find_by_id(id)
        except Exception as e:
            return e

    @classmethod
    def find_by_stuff_id(cls, stuff_id):
        try:
            da = StorageDa()
            return da.find_by_stuff_id(stuff_id)
        except Exception as e:
            return e

    @classmethod
    def find_by_count(cls, count):
        try:
            da = StorageDa()
            return da.find_by_count(count)
        except Exception as e:
            return e
