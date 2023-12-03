from model.da.person_da import PersonDa
from model.entity.person import Person


class PersonController:
    @classmethod
    def save(cls, name, family, phone_number, email, username, password):
        try:
            person = Person( name, family, phone_number, email, username, password)
            da = PersonDa()
            da.save(Person)
            return True, Person
        except Exception as e:
            return e

    @classmethod
    def edit(cls, id, name, family, phone_number, email, username, password, active):
        try:
            da = PersonDa()
            Person = da.find_by_id(id)
            Person.name = name
            Person.family = family
            Person.phone_number = phone_number
            Person.email = email
            Person.username = username
            Person.password = password
            Person.active = active
            da.edit(Person)
            return True, Person
        except Exception as e:
            return e

    @classmethod
    def remove(cls, id):
        try:
            da = PersonDa()
            person = da.find_by_id(id)
            da.remove(id)
            return True, id
        except Exception as e:
            return e

    @classmethod
    def find_all(cls):
        try:
            da = PersonDa()
            return da.find_all()
        except Exception as e:
            return e

    @classmethod
    def find_by_person_id(cls, id):
        try:
            da = PersonDa()
            return da.find_by_id(id)
        except Exception as e:
            return e

    @classmethod
    def find_by_name(cls, name):
        try:
            da = PersonDa()
            return da.find_by_name(name)
        except Exception as e:
            return e

    @classmethod
    def find_by_family(cls, family):
        try:
            da = PersonDa()
            return da.find_by_family(family)
        except Exception as e:
            return e

    @classmethod
    def find_by_phone_number(cls, phone_number):
        try:
            da = PersonDa()
            return da.find_by_phone_number(phone_number)
        except Exception as e:
            return e

    @classmethod
    def find_by_email(cls, email):
        try:
            da = PersonDa()
            return da.find_by_email(email)
        except Exception as e:
            return e

    @classmethod
    def find_by_username(cls, username):
        try:
            da = PersonDa()
            return da.find_by_username(username)
        except Exception as e:
            return e

    @classmethod
    def find_by_password(cls, password):
        try:
            da = PersonDa()
            return da.find_by_password(password)
        except Exception as e:
            return e

    @classmethod
    def find_by_active(cls, active):
        try:

            da = PersonDa()
            return da.find_by_active(active)
        except Exception as e:
            return e
