from model.da.database import DataBaseManager
from model.entity.storage import Storage


class StorageDa(DataBaseManager):
    def find_by_stuff_id(self, stuff_id):
        self.make_engine()
        result = self.session.query(Storage).filter(Storage.stuff_id == stuff_id)
        self.session.close()
        return result

    def find_by_count(self, count):
        self.make_engine()
        result = self.session.query(Storage).filter(Storage.count == count)
        self.session.close()
        return result
