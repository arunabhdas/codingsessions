from dataclasses import dataclass

@dataclass
class Person:
    firstname: str
    lastname: str
    age: int

    def printname(self):
        print(f'{self.firstname} {self.lastname}')
        
        
if __name__ == '__main__':
    x = Person('John', 'Doe', 40)
    x.firstname = 'Jane'
    print(x)
    