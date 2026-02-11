class person: #parent class
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def printname(self):
        print(self.name, self.surname) 

class student(person): #child class, which will inherit the properties and methods from the person class.
    def __init__(self, name, surname): #when we write init in child class it overrides parents class
        person.__init__(self, name, surname) #but we can inherit in there like that

x = student("Kanye", "West")
x.printname()
