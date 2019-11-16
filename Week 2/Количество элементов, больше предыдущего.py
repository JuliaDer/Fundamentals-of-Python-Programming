prev = int(input())
answer = 0
while prev != 0:
    next1 = int(input())
    if next1 != 0 and prev < next1:
        answer += 1
    prev = next1
print(answer)
