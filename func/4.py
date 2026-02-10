def my_function(name, /): #if you what only positional you need to use ,/ after arguments
  print("Hello", name)

my_function("Kendrick") 

def my_function(*, name): #and vice versa you need to use *, before arguments
  print("Hello", name)

my_function(name = "Kendrick")