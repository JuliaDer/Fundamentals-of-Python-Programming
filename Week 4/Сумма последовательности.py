def sum():
    global s
    n = int(input())
    if n != 0:
        s += n
        sum()
    if n == 0:
        print(s)


s = 0
sum()
