from model.da.transaction_da import TransactionDa
from model.entity.transaction import Transaction


class TransactionController:
    @classmethod
    def save(cls, person_id, stuff_id, date_time, count, type):
        try:
            transaction = Transaction()
            transaction.person_id = person_id
            transaction.stuff_id = stuff_id
            transaction.date_time = date_time
            transaction.count = count
            transaction.type = type
            da = TransactionDa()
            da.save(Transaction)
            return True, Transaction
        except Exception as e:
            return e

    @classmethod
    def edit(cls, id, person_id, stuff_id, date_time, count, type):
        try:
            da = TransactionDa()
            Transaction = da.find_by_id(id)
            Transaction.person_id = person_id
            Transaction.stuff_id = stuff_id
            Transaction.date_time = date_time
            Transaction.count = count
            Transaction.type = type
            da.edit(Transaction)
            return True, Transaction
        except Exception as e:
            return e

    @classmethod
    def remove(cls, id):
        try:
            da = TransactionDa()
            Transaction = da.find_by_id(id)
            da.remove(id)
            return True, id
        except Exception as e:
            return e

    @classmethod
    def find_by_id(cls, id):
        try:
            da = TransactionDa()
            return da.find_by_id(id)
        except Exception as e:
            return e

    @classmethod
    def find_by_person_id(cls, person_id):
        try:
            da = TransactionDa()
            return da.find_by_person_id(person_id)
        except Exception as e:
            return e

    @classmethod
    def find_by_stuff_id(cls, stuff_id):
        try:
            da = TransactionDa()
            return da.find_by_stuff_id(stuff_id)
        except Exception as e:
            return e

    @classmethod
    def find_by_date_time(cls, date_time):
        try:
            da = TransactionDa()
            return da.find_by_date_time(date_time)
        except Exception as e:
            return e

    @classmethod
    def find_by_count(cls, count):
        try:
            da = TransactionDa()
            return da.find_by_count(count)
        except Exception as e:
            return e

    @classmethod
    def find_by_type(cls, type):
        try:
            da = TransactionDa()
            return da.find_by_type(type)
        except Exception as e:
            return e
