from model.da.transaction_da import *
from model.entity.transaction import Transaction


class TransactionController:
    @classmethod
    def save(cls, person_id, stuff_id, date_time, count, t_type):
        try:
            person_da = PersonDa()
            person = person_da.find_by_id(Person,person_id)
            person_da.session.close()
            print(person)

            stuff_da = StuffDa()
            stuff = stuff_da.find_by_id(Stuff,stuff_id)
            stuff_da.session.close()
            print(stuff)

            transaction = Transaction(person,stuff,count,t_type)
            da = TransactionDa()
            da.save(transaction)
            return True, transaction
        except Exception as e:
            return False,str(e)

    @classmethod
    def edit(cls, id, person_id, stuff_id, date_time, count, t_type):
        try:
            da = TransactionDa()
            transaction = da.find_by_id(Transaction,id)
            transaction.person_id = person_id
            transaction.stuff_id = stuff_id
            transaction.date_time = date_time
            transaction.count = count
            transaction.t_type = t_type
            da.edit(transaction)
            return True, transaction
        except Exception as e:
            return False,str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = TransactionDa()
            transaction = da.find_by_id(Transaction,id)
            da.remove(id)
            return True, id
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_all(cls):
        try:
            da = TransactionDa()
            return da.find_all(Transaction)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = TransactionDa()
            return da.find_by_id(Transaction,id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_person_id(cls, person_id):
        try:
            da = TransactionDa()
            return da.find_by_person_id(person_id)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_stuff_id(cls, stuff_id):
        try:
            da = TransactionDa()
            return da.find_by_stuff_id(stuff_id)
        except Exception as e:
             return False,str(e)

    @classmethod
    def find_by_date_time(cls, date_time):
        try:
            da = TransactionDa()
            return da.find_by_date_time(Transaction,date_time)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_count(cls, count):
        try:
            da = TransactionDa()
            return da.find_by_count(Transaction,count)
        except Exception as e:
            return False,str(e)

    @classmethod
    def find_by_type(cls, t_type):
        try:
            da = TransactionDa()
            return da.find_by_type(Transaction,t_type)
        except Exception as e:
            return False,str(e)
