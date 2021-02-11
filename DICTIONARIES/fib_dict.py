# create a dictionary representing the first 12 values of the fibonacci sequence

n = 12
x = 0
y = 1
d = dict()
for _ in range(1, n+1):
    d[_] = x
    x, y = y, x+y
print(d)