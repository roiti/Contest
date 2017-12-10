# -*- coding: utf-8 -*-
N, K = map(int, raw_input().split())    
ab = [map(int, raw_input().split()) for i in xrange(N)]
ab.sort()
for a, b in ab:
    if K <= b:
        print a
        break
    else:
        K -= b
