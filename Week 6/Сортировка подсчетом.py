def count_sort(num):
    sorted_list = [0] * 101
    for i in num:
        sorted_list[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sorted_list[i], end='')


num = [int(i) for i in input().split()]
count_sort(num)
