import math
x = float(input())
b = x * 100
a = math.ceil(b // 100)
m = math.ceil(b % 100)
print(a, m)
