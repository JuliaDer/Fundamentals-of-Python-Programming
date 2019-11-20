P = int(input())
X = int(input())
Y = int(input())
K = int(input())
i = 1
total = X * 100 + Y
percent = int(total * (100 + P) / 100)
percentT = 0
if K > i:
    while i != K:
        percentT = (percent * (100 + P) / 100)
        percent = percentT // 1
        i += 1
    percentT = int(percentT)
else:
    percentT = int(percent)
print(percentT // 100, percentT % 100)
