a = input().split()
b = [x for x in a if x != '0']
b.extend(x for x in a if x == '0')

print(' '.join(b))
