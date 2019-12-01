def perimeter(x1, y1, x2, y2, x3, y3):
    dist1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    dist2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** (1 / 2)
    dist3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)
    return dist1 + dist2 + dist3


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
print(perimeter(x1, y1, x2, y2, x3, y3))
