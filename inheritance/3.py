class Person:
    def __init__(self, name):
        self.name = name
        print("Person created")

class Student(Person):
    def __init__(self, name, grade): #overriding persons init
        self.grade = grade
        self.name = name
        print("Student added")
        

s = Student("Sanzhar", 21)

print(s.name)
print(s.grade)