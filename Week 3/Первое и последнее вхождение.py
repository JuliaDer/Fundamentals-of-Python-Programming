string = input()
pos = 0
s1 = string.find('f')
s2 = string.rfind('f')
if s1 == -1:
    print()
elif s1 == s2:
    print(s1)
else:
    print(s1, s2)
