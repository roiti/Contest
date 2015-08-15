N, A, B = map(int, raw_input().split())
S = [int(raw_input()) for i in xrange(N)]
s = sum(S)
mx, mn = max(S), min(S)
if mx == mn:
    print -1
else:
    P = float(B) / (mx - mn)
    Q = (N * A - P * s) / N
    print "%.10f %.10f" % (P, Q)
