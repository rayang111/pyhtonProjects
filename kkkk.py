a = int(input("A ?"))
b = int(input("B ?"))
c = int(input("C ?"))

MAX = 0

if (a >= b) and (a >= c):
    MAX = a
if (b >= a) and (b >= c):
    MAX = b
if (c >= a) and (c >= b):
    MAX = c

print(MAX)


