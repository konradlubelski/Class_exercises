import random
from datetime import datetime

class Single_Contact(object):

    def __init__(self, name, surname):
        now = datetime.now()
        self.name = name
        self.surname = surname
        self.email = name + surname + "@gmail.com"
        self.creation_date = now.strftime("%d/%m/%Y, %H:%M:%S")

    def modify(self):
        now = datetime.now()
        name = self.name + "L"
        modification_date = now.strftime("%d/%m/%Y, %H:%M:%S")
        return name, modification_date

person_1 = Single_Contact("Jan", "Kowalski",)
person_2 = Single_Contact("Konrad", "Lubelski")
person_3 = Single_Contact("Damian", "Lubelski")
print(person_2.__dict__)
print(person_2.modify())

