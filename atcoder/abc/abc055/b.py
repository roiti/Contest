# -*- coding: utf-8 -*-
mod = 10**9 + 7
N = int(raw_input())

ans = 1
for i in xrange(2, N + 1):
    ans = ans*i % mod
print ans
