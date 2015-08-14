import math
pi = math.pi
N = int(raw_input())
R = [0] + sorted([int(raw_input()) for i in xrange(N)])
ans = 0
while len(R) > 1:
    r2, r1 = R.pop(), R.pop()
    ans += (r2 * r2 - r1 * r1) * pi
print "%.10f" % ans
