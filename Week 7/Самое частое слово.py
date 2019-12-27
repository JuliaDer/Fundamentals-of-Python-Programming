fin = open('input.txt')
s = fin.readlines()
ans = []
for i in s:
    for j in i.strip().split():
        ans.append(j)
words = set(ans)
keys = [i for i in range(len(words))]
help = [0 for i in range(len(words))]
slov = dict(zip(words, keys))
for i in ans:
    if i in slov.keys():
        help[slov.get(i)] += 1
c = dict(zip(words, help))
b = list(c.items())
b.sort(key=lambda x: (-x[1], x[0]))
print(b[0][0])
