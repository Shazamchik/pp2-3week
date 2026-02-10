def func(salem, *names): # *names mean *args(arbitrary arguments) allow functions to accept a unknown number of arguments, tuple.
    for name in names:
        print(salem, name)
func("Salem", "Beiba", "Ilyas", "Zhasmin")

def func2(**names): # **names means **kwargs(keyword arbitrary arguments) that allows to accept a unknown number of keyword arguments, dictionary
    print("Salem my bro" + " " + names["name2"])
func2(name1 = "Askan", name2 = "Nargiz")