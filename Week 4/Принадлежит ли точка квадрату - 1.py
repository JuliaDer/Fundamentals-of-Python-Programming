def is_point_in_square(x, y):
    return abs(x) <= 1 and abs(y) <= 1


a = float(input())
b = float(input())
if is_point_in_square(a, b):
    print('YES')
else:
    print('NO')
