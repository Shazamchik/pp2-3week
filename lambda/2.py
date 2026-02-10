numbers = list(map(int, input().split())) #takes values from input people
doubled = list(map(lambda x: x * 2, numbers)) #multiply every x by 2
print(doubled)