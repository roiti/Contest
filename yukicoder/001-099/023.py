import math
H,A,D = map(int,raw_input().split())
ans = 10**10
for a in xrange(10001):
    h = H-a*A
    if h < 0:
        ans = min(ans, a)
        break
    ans = min(ans, 3./2.*math.ceil(1.0*h/D)+a)
print ans