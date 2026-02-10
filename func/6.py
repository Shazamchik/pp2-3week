x = 300 #global scope, that can use everyone

def myfunc():
  x = 200 #local scope, that can use only in this func
  print(x)

myfunc()

print(x)