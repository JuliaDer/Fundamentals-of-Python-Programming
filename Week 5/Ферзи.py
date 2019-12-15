x, y = [], []
flag = False

for i in range(8):
    a, b = [int(j) for j in input().split()]
    x.append(a)
    y.append(b)
for i in range(8):
    for j in range(i + 1, 8):
        if x[i] == x[j] or y[i] == y[j] or \
                abs(x[i] - x[j]) == abs(y[i] - y[j]):
            flag = True
if flag:
    print('YES')
else:
    print('NO')
