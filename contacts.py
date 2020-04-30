import random
from datetime import datetime


class Single_Contact(object):

    def __init__(self, name, surname, group):
        now = datetime.now()
        self.name = name
        self.surname = surname
        self.group = group
        self.email = name + surname + "@gmail.com"
        self.creation_date = now.strftime("%d/%m/%Y, %H:%M:%S")

    def modify(self):
        now = datetime.now()
        name = self.name + "L"
        modification_date = now.strftime("%d/%m/%Y, %H:%M:%S")
        return name, modification_date

person_1 = Single_Contact("Jan", "Kowalski","family")
person_2 = Single_Contact("Konrad", "Lubelski","family")
person_3 = Single_Contact("Damian", "Lubelski","work")
print(person_2.__dict__)
print(person_2.modify())

class ContactsGroup(object):

    def __init__(self, contact_group_name):
        self.contact_group_name=contact_group_name
        
    def create(self):
        self.list = []

    def read(self):
        return self.list

    def update(self, person):
        if person not in self.list and person.group == self.contact_group_name :
            self.list.append(person)

    def remove(self, person):
        if person in self.list:
            self.list.remove(person)

    def print_group(self):
        print(self.list)

        
group_1 = ContactsGroup("family")
group_1.create()
group_1.update(person_2)
group_1.update(person_1)
group_1.update(person_3)
print (repr(group_1.read()))

