from model.da.person_da import PersonDa
from model.entity.person import Person


class PersonController:
    @classmethod
    def save(cls, name, family, phone_number, email, username, password, active=True):
        try:
            person = Person(name, family, phone_number, email, username, password, active)
            da = PersonDa()
            da.save(person)
            return True, person
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, phone_number, email, username, password, active=True):
        try:
            da = PersonDa()
            person = Person(name, family, phone_number, email, username, password, active)
            person.id = id
            da.edit(person)
            return True, person
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = PersonDa()
            person = da.find_by_id(Person, id)
            da.remove(person)
            return True, person
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = PersonDa()
            return da.find_all(Person)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = PersonDa()
            return da.find_by_id(Person, id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = PersonDa()
            return da.find_by_name(name)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(cls, family):
        try:
            da = PersonDa()
            return da.find_by_family(family)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            da = PersonDa()
            return da.find_by_phone_number(phone_number)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_email(cls, email):
        try:
            da = PersonDa()
            return da.find_by_email( email)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = PersonDa()
            return da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_password(cls,username, password):
        try:
            da = PersonDa()
            return da.find_by_username_password(username,password)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_active(cls, active):
        try:
            da = PersonDa()
            return da.find_by_active(active)
        except Exception as e:
            return False, str(e)
