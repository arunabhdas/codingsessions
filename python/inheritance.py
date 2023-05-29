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

    def printname_and_language(self):
        print(f'{self.firstname} {self.lastname} loves {self.favelanguage}')



if __name__ == '__main__':
    p1 = Person('John', 'Doe')
    p1.printname()

    p2 = Programmer('Jane', 'Doe', 'Python')
    p2.printname_and_language()
    
     