n = [int(i) for i in input().split()]
for i in range(len(n)):
    if n.count(n[i]) == 1:
        print(n[i], end=' ')
