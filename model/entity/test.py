from model.da.database import DataBaseManager
from model.entity import *

da = DataBaseManager()
da.make_engine()

# person = da.find_by_id(Person,1)
#
# print(person)
# print(person.transaction)

# transaction = da.find_by_id(Transaction,1)
# print(transaction)
# print(transaction.stuff)
# print(transaction.person)

# person = Person("A","A",1234,"AAA","A","A")
# da.save(person)
# print(person)
#
# group1 = StuffGroup("root")
# da.save(group1)
# print(group1)
#
# group2 = StuffGroup("barghi",group1)
# da.save(group2)
# print(group2)

#
# stuff = Stuff("ss","bbb","dddd",group1)
# da.save(stuff)
# print(stuff)
#
# transaction = Transaction(person,stuff,5,"in")
# da.save(transaction)
# print(transaction)
#
# storage = Storage(stuff,5)
# da.save(storage)
# print(storage)

