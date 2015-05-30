def e_gcd(a, b):
    u0, u1 = 1,0
    if b == 0:
        return u0,u1

    d0, d1 = a,b
    while True:
        q,r = d0 // d1, d0 % d1
        if r == 0:
            return u1,(d1-a*u1)/b

        d0, d1 = d1, r
        u0, u1 = u1, u0 - q * u1

a,b = map(int, raw_input().split())
print " ".join(map(str, e_gcd(a,b)))
