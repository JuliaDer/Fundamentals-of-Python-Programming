n = int(input())
step = 1
maxStep = 1
while step <= n:
    step = step * 2
step = step // 2
if step == n:
    print('YES')
else:
    print('NO')
