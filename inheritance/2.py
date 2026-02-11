class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hunt(self):
        print("animal is hunting")
class wolf(animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def howl(self):
        print("Wolf is howling")
n = wolf("Alpha", 15)
print(n.name)
print(n.age)
n.howl()
n.hunt()