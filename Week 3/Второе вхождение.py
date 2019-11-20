s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
#  Без метода 'count'
s = input()
num = 0
for i in range(len(s)):
    if s[i] == "f":
        num += 1
        if num == 2:
            print(i)
if num == 1:
    print('-1')
elif "f" not in s:
    print('-2')
