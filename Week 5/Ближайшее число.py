n = int(input())
numbers = map(int, input().split())
x = int(input())
print(min(numbers, key=lambda a: abs(a-x)))
