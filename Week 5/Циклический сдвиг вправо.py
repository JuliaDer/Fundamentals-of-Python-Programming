n = list(input().split())
w = n[len(n)-1]
n.pop()
n.insert(0, w)
print(*n)
