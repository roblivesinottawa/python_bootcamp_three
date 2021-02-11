import random
import matplotlib.pyplot as plt

k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = {}

for letter in k:
    d[letter] = random.randint(1, 100)

print(d)

x, y = zip(*d.items())
plt.bar(x, y)