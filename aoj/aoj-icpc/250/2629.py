import math
d = float(raw_input())
ans = math.sqrt(2) * d
for x in xrange(1, 11):
    if x * x <= d * d <= x * 2 + 1:
        ans = max(ans, x + 1)
print "%.10f" % ans
