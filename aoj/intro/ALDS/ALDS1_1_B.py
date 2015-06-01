def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

a, b = map(int, raw_input().split())
print gcd(a, b)

