cost1 = int(input())
cost2 = int(input())
n = int(input())
totalCost = cost1 * 100 + cost2
print((totalCost * n) // 100, (totalCost * n) % 100)
