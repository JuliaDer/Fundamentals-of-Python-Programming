print(*map(lambda a, b: int(a != b),
           list(map(int, input().split())), list(map(int, input().split()))))
