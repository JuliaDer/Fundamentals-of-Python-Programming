n = [int(s) for s in input().split()]
height = int(input())
counter = 0

for i in n:
    if i < height:
        n.insert(counter, height)
        break
    counter += 1

print(counter + 1)
