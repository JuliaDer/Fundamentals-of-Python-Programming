import math

x = float(input())
y = (x * 100) % 100
if y < 50:
    print(int(x))
if y >= 50:
    print(math.ceil(x))
