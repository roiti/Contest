# -*- coding: utf-8 -*-
N, M = map(int, raw_input().split())
cnt = [0]*N
for loop in xrange(M):
    a, b = map(int, raw_input().split())
    cnt[a - 1] += 1
    cnt[b - 1] += 1
for i in cnt:
    print i

