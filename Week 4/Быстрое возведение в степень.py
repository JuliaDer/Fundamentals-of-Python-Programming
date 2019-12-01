def quick_power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return quick_power(x, n / 2)**2
    else:
        return x * quick_power(x, n-1)


print(quick_power(float(input()), int(input())))
