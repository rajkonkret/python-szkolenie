
#klasa to nowy typ
class Person:
    #specjalna metoda __init__
    def __init__(self,name,surname,pesel):
        self.name = name
        self.surname = surname
        self.pesel = pesel

p = Person('Adam','Kowalski','1234567890')
print(p.surname)
print(p.name)