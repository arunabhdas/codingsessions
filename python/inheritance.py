class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(f'{self.firstname} {self.lastname}')

class Programmer(Person):
    def __init__(self, firstname, lastname, favelanguage):
        super().__init__(firstname, lastname)
        self.favelanguage = favelanguage

    def printname(self):
        print(f'{self.firstname} {self.lastname} loves {self.favelanguage}')

