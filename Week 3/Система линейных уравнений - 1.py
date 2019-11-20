# def delete_zeros(x):
#     if x == int(x):
#         x = int(x)
#     elif len(str((x - int(x)))) > 8:
#         if x < 1:
#             x = (int(x * 10 ** 6)) / (10 ** 6)
#         else:
#             x = (int(x * 10 ** 5)) / (10 ** 5)
#     else:
#         x = str(x)
#         while x[-1] == '0':
#             x = x[:-1]
#     return x


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

y = (a * f - c * e) / (a * d - b * c)

if a != 0:
    x = (e - b * y) / a
else:
    x = (c * d - b * f) / (a * d - b * c)
    y = (e - a * x) / b

print(x, y)
# print(delete_zeros(x), delete_zeros(y))
