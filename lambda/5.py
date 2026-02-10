def myfunc(n):
  return lambda a : a * n # k  will be in place of n, a: a * k, then m will be in a and will return the total.

k, m = map(int, input().split())

mydoubler = myfunc(k)

print(mydoubler(m))