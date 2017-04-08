# -*- coding: utf-8 -*-
zero = "CEFGHIJKLMNSTUVWXYZ"
one = "ADOPQR"
two = "B"

N, D = map(int, raw_input().split())
ans = ["A"]*N
D -= N
for i in xrange(N - 1, -1, -1):
    if D > 0:
        ans[i] = "B"
        D -= 1
    elif D < 0:
        ans[i] = "C"
        D += 1
print "".join(ans)
