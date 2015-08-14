def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

N = int(raw_input())
xy = [map(int, raw_input().split()) for i in xrange(N)]
ans = 0
for i in xrange(N):
    for j in xrange(i + 1, N):
        ans = max(ans, dist(xy[i], xy[j]))
print "%.10f" % ans
