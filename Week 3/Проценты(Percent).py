P = int(input())
X = int(input())
Y = int(input())
total = X * 100 + Y
dep = int(total * (100 + P) / 100)
print(dep // 100, ' ', dep % 100, sep='')
