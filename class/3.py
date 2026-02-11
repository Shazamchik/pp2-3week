class Dog:
    def __init__(self, name, age): #self need to be always first parameter bur you can name it as you want
        self.name = name
        self.age = age
    def bark (self):
        print(self.name, "says Woof!")
n = Dog("Aktos", 3)
print(n.age) 
n.bark() 