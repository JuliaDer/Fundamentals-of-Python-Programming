n = [int(i) for i in input().split()]
counter = 0

for i in range(len(n) - 1):
    if n[i] != n[i+1]:
        counter += 1

print(counter + 1)
