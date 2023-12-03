from model.entity.person import Person
from model.da.database import DataBaseManager


class PersonDa(DataBaseManager):

    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Person).filter(Person.name.like(name))
        self.session.close()
        return result

    def find_by_family(self, family):
        self.make_engine()
        result = self.session.query(Person).filter(Person.family.like(family))
        self.session.close()
        return result

    def find_by_phone_number(self, phone_number):
        self.make_engine()
        result = self.session.query(Person).filter(Person.phone_number == phone_number)
        self.session.close()
        return result

    def find_by_email(self, email):
        self.make_engine()
        result = self.session.query(Person).filter(Person.email.like(email))
        self.session.close()
        return result

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Person).filter(Person.username.like(username))
        self.session.close()
        return result

    def find_by_password(self, password):
        self.make_engine()
        result = self.session.query(Person).filter(Person.password == password)
        self.session.close()
        return result

    def find_by_active(self, active):
        self.make_engine()
        result = self.session.query(Person).filter(Person.active == active)
        self.session.close()
        return result
