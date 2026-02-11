class pers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
n = pers("Beka", 19)

del n.age #deleting age

print(n.name) 

#print(n.age)  # causes an error  