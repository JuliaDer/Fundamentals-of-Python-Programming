def merge(a, b):  # First example
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

print(*merge(list_a, list_b))


def merger(a, b):  # Second example
    new_list = []
    d = a + b
    while d:
        new_list.append(d.pop(d.index(min(d))))
    return new_list


list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
print(*merger(list_a, list_b))
