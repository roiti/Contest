N, va, vb, L = map(int, raw_input().split())
for loop in xrange(N):
    t = float(L) / va
    L = vb * t
print "%.10f" % L
