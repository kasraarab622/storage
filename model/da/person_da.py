from model.entity import *
from model.da import *

class PersonDa(DataBaseManager):

    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Person).filter(Person.name.like(name+"%")).all()
        return result

    def find_by_family(self, family):
        self.make_engine()
        result = self.session.query(Person).filter(Person.family.like(family+"%")).all()
        return result

    def find_by_phone_number(self, phone_number):
        self.make_engine()
        result = self.session.query(Person).filter(Person.phone_number == phone_number).all()
        return result

    def find_by_email(self, email):
        self.make_engine()
        result = self.session.query(Person).filter(Person.email.like(email)).all()
        return result

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Person).filter(Person.username.like(username)).all()
        return result

    def find_by_username_password(self,username, password):
        self.make_engine()
        result = self.session.query(Person).filter(and_(Person.username == username, Person.password == password)).all()
        return result

    def find_by_active(self, active):
        self.make_engine()
        result = self.session.query(Person).filter(Person.active == active).all()
        return result
