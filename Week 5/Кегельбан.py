a = [int(i) for i in input().split()]
b = ['I'] * a[0]

for i in range(a[1]):
    c = [int(i) for i in input().split()]
    for j in range(c[0], c[1] + 1):
        b[j - 1] = '.'

print(''.join(b))
