n = [int(i) for i in input().split()]
counter = 0
for i in n:
    for j in n:
        if i == j:
            counter += 1
    counter -= 1

print(counter // 2)
