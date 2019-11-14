time = int(input())
hours = time // 3600 % 24
min1 = time // 60 % 60 // 10
min2 = time // 60 % 60 % 10
sec1 = time % 60 // 10
sec2 = time % 10
print(hours, ':', min1, min2, ':', sec1, sec2, sep='')
