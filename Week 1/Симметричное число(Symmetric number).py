n = int(input())
m = (n // 1000) * 10
k = (n % 1000) // 100
t = (n % 100) // 10
r = (n % 10) * 10
print(((m + k) - (t + r)) + 1)
