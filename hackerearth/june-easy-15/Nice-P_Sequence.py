def gcd(a, b):
    while b: a, b = b, a % b
    return a

def extgcd(a, b):
    u0, u1 = 1,0
    if b == 0:
        return u0,u1

    d0, d1 = a, b
    while 1:
        q,r = d0 / d1, d0 % d1
        if r == 0:
            return u1, (d1 - a * u1) / b

        d0, d1 = d1, r
        u0, u1 = u1, u0 - q * u1

def mod_inverse(a, p):
    x, y = extgcd(a, p)
    return (p + x % p) % p

T = int(raw_input())
for loop in xrange(T):
    a, p, n = map(int, raw_input().split())
    if gcd(a, p) != 1:
        print -1
        continue

    b = mod_inverse(a, p)
    ans = (a + b) * (n / 2) + (a if n % 2 else 0)
    print ans
