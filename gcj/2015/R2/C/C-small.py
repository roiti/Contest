import sys, math, re, itertools as it, bisect, string
from collections import (defaultdict, deque)

T = int(raw_input())
for case in xrange(1, T + 1):
    N = int(raw_input())
    E = set(raw_input().split())
    F = set(raw_input().split())

    if N == 2:
        ans = len(E & F)
    else:
        ans = 10 ** 10
    s = [set(raw_input().split()) for i in xrange(N - 2)]
    for bit in it.product([0, 1], repeat = N - 2):
        e, f = E.copy(), F.copy()
        for i in xrange(N - 2):
            if bit[i] == 0:
                e |= s[i]
            else:
                f |= s[i]
        ans = min(ans, len(e & f))
    print "Case #%d: %d" % (case, ans)
