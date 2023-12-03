from controller.person_controller import PersonController
from model.da.database import DataBaseManager
from model.entity.person import Person
from model.entity.storage import Storage
from model.entity.stuff import Stuff
from model.entity.transaction import Transaction

da = DataBaseManager()


# person = Person("ahmad", "messbah","09178505323","messbah.a@gmail.com","ahmad","ahmad123")
# da.save(person)
# print(person.id)
#
# stuff = Stuff("mobile","samsung","description",1)
# da.save(stuff)
# print(stuff.id)
#
# storage = Storage(stuff.id, 10)
# da.save(storage)
print(PersonController.save("ahmad", "messbah", "09178505323", "messbah.a@gmail.com", "ahmad", "ahmad123"))