N = int(raw_input())
a = b = c = d = e = f = 0
for loop in xrange(N):
    M, m = map(float, raw_input().split())
    if   M >= 35: a += 1
    elif M >= 30: b += 1
    elif M >= 25: c += 1
    if   m >= 25: d += 1
    if   M >= 0 and m < 0: e += 1
    if   M < 0: f += 1
print a, b, c, d, e, f
