from model.da.database import DataBaseManager
from model.entity.transaction import Transaction

class TransactionDa(DataBaseManager):

    def find_by_person_id(self,person_id):
        self.make_engine()
        result = self.session.query(Transaction).filter(Transaction.person_id == person_id)
        self.session.close()
        return result

    def find_by_stuff_id(self,stuff_id):
        self.make_engine()
        result = self.session.query(Transaction).filter(Transaction.stuff_id == stuff_id)
        self.session.close()
        return result
    def find_by_stuff_count(self,stuff_count):
        self.make_engine()
        result = self.session.query(Transaction).filter(Transaction.stuff_count == stuff_count)
        self.session.close()
        return result
    def find_by_date_time(self,date_time):
        self.make_engine()
        result = self.session.query(date_time).filter(Transaction.date_time == date_time)
        self.session.close()
        return result

    def find_by_count(self,count):
        self.make_engine()
        result =self.session.query(Transaction).filter(Transaction.count == count)
        self.session.close()
        return result

    def find_by_type(self,type):
        self.make_engine()
        result =self.session.query(Transaction).filter(Transaction.type.like(type))
