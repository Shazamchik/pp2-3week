class greating:
    def __init__(self, name): # runs automatically when object is created
        self.name = name # save the name passed to the object
    def func(self):
        print("Salem "+ self.name + ". " + "Kalaisyn?" )
n = greating("Azamat") # create an object 
n.func()