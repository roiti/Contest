import math
def gcd(a, b):
    while b: a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)
    
n = int(raw_input())
f = map(int, raw_input().split())
loop = [1] * n
where = [1] * n
for i in xrange(n):
    hist = [f[i]]
    a = f[i]
    for j in xrange(1, 10 * n):
        a = f[a - 1]
        if a in hist:
            loop[i] = j - hist.index(a)
            where[i] = hist.index(a) + 1
            break
        hist.append(a)

ans = 1
start = max(where)
whole = 1
for i in xrange(n):
    whole = lcm(whole, loop[i])
whole *= max(1, int(math.ceil(1.0 * start/whole)))
print whole
