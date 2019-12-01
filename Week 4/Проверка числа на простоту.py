def is_prime(n):
    i = 1
    while i != n:
        i += 1
        if n % i == 0:
            if i != n:
                return 1
        if i >= n ** (1 / 2):
            return 0


a = int(input())

print("NO" if is_prime(a) else "YES")
