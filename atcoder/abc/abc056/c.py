# -*- coding: utf-8 -*-
X = int(raw_input())

ans = 10**8
lo, hi = 1, 10**10
while hi - lo >= 1:
    mi = (hi + lo)/2
    if X - mi <= (mi - 1)*mi/2:
        ans = min(ans, mi)
        hi = mi
    else:
        lo = mi + 1
print ans
