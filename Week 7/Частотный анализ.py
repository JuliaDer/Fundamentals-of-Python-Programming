fin = open('input.txt')
s = fin.readlines()
ans = []
for i in s:
    for j in i.strip().split():
        ans.append(j)
lst = sorted(set(ans), key=lambda x: (-ans.count(x), x))
for i in lst:
    print(i)
