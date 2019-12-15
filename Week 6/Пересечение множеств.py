list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

print(*sorted(list(set(list_a).intersection(list_b))))
