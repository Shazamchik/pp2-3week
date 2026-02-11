class Person:
    grade = 11 # Class property

    def __init__(self, name):
        self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.grade)
print(p2.grade)