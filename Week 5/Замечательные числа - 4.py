num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    if i // 100 == (i % 10) * 10 + (i % 100) // 10:
        print(i)
