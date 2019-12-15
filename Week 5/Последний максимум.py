a = [int(i) for i in input().split()]
index_of_max = 0
max_num = a[0]
for i in range(1, len(a)):
    if a[i] >= max_num:
        max_num = a[i]
        index_of_max = i
print(a[index_of_max], index_of_max)
