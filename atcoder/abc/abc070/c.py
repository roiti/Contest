def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

N = int(raw_input())
T = [int(raw_input()) for i in xrange(N)]

print reduce(lcm, T)
