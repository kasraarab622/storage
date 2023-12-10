from model.entity import *
from model.da import *


person = Person("Asdfsdfsdfsdf","Asdfsdf",345435,"sreergA","A","A")
# person.id = 1
da = PersonDa()
da.save(person)
# da.edit(person)
# print(person)
print(da.find_all(Person))