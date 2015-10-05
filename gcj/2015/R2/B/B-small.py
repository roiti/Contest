import sys, math, re, itertools as it, bisect, string
from collections import (defaultdict, deque)

T = int(raw_input())
for case in xrange(1, T + 1):
    N, V, X = raw_input().split()
    N, V, X = int(N), float(V), float(X)
    RC = [map(float, raw_input().split()) for i in xrange(N)]

    ans = 10 ** 18
    if N == 1:
        if X != RC[0][1]:
            print "Case #%d: %s" %(case, "IMPOSSIBLE")
            continue
        else:
            ans = V / RC[0][0]
    elif N == 2:
        R0, C0 = RC[0]
        if X == C0:
            ans = min(ans, X / R0)
        R1, C1 = RC[1]
        if X == C1:
            ans = min(ans, X / R1)
        if X == C0 == C1:
            ans = min(ans, X / (R0 + R1))
        try:
            s0 = V * (X - C1) / (R0 * C0 - R0 * C1)
            s1 = (V - s0 * R0) / R1
            if not (min(s0, s1) < 0
                or abs(V - (s0 * R0 + s1 * R1)) > 1e-7
                or abs(X - (s0 * R0 * C0 + s1 * R1 * C1) / (s0 * R0 + s1 * R1)) > 1e-7):
                ans = min(ans, max(s0, s1))
        except:
            pass
        try:
            s1 = V * (X - C0) / (R1 * C1 - R1 * C0)
            s0 = (V - s1 * R1) / R0
            if not (min(s0, s1) < 0
                or abs(V - (s0 * R0 + s1 * R1)) > 1e-7
                or abs(X - (s0 * R0 * C0 + s1 * R1 * C1) / (s0 * R0 + s1 * R1)) > 1e-7):
                ans = min(ans, max(s0, s1))
        except:
            pass
        if ans == 10 ** 18:
            print "Case #%d: %s" % (case, "IMPOSSIBLE")
            continue
    print "Case #%d: %.10f" % (case, ans)
