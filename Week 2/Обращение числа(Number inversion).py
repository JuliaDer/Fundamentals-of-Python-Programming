#  One example
a = int(input())
one = 0
while a != 0:
    one = a % 10
    print(one, end="")
    a = a // 10
#  Second example
num = input("Введите число: ")
print("".join(reversed(num)))
