class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, "barks")
class Run:
    def __init__(self, name):
        self.name = name
    def run(self):
        print(self.name, "is running")
class dog(animal, Run): #we can give multiple parents like that
    pass
n = dog("Aktos")

n.speak()
n.run()