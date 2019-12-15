import sys

n = int(input())
message = sys.stdin.readlines()
ans = []
for i in range(len(message)):
    b1 = int(message[i].split()[-1])
    b2 = int(message[i].split()[-2])
    b3 = int(message[i].split()[-3])
    sum = b1 + b2 + b3
    if b1 >= 40 and b2 >= 40 and b3 >= 40:
        ans.append(sum)
fig = sorted(ans, reverse=True)
if len(fig) <= n:
    print(0)
elif fig.count(max(fig)) > n:
    print(1)
elif fig[n] == fig[n - 1]:
    j = 1
    while fig[n - j + 1] == fig[n - j]:
        j += 1
    print(fig[n - j])
else:
    print(fig[n - 1])
