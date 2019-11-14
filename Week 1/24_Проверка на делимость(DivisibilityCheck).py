n = int(input())
m = int(input())
k = n % m
print((0 ** k) * 'YES', (1 - 0 ** k) * 'NO')
