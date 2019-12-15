n = [int(i) for i in input().split()]
for i in range(len(n)):
    if n[i] == max(n):
        index_max = i
    if n[i] == min(n):
        index_min = i

n[index_max], n[index_min] = n[index_min], n[index_max]
print(' '.join(str(i) for i in n))
