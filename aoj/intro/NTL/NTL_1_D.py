def phi(n):
    r = n
    i = 2
    while i * i <= n:
        if n % i==0:
            r -= r / i
            while n % i==0:
                n /= i
        i += 1
    if n > 1: r -= r / n
    return r

n = int(raw_input())
print phi(n)
