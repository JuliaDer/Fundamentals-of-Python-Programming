space_and_user = list(map(int, input().split()))
s = space_and_user[0]
n = space_and_user[1]
t = []
numUser = 0
sumUser = 0
pukUser = 0
while numUser < n:
    vUser = int(input())
    numUser += 1
    t.append(vUser)
t.sort()
for i in t:
    if sumUser < s:
        sumUser += i
        if sumUser < s:
            pukUser += 1
print(pukUser)
