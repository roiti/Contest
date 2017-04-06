# -*- coding: utf-8 -*-
K, S = map(int, raw_input().split())
ans = 0
for X in xrange(0, K + 1):
    for Y in xrange(0, min(K + 1, S - X + 1)):
        if 0 <= S - (X + Y) <= K:
            ans += 1
print ans
