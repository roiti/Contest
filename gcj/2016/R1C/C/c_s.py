# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for case in xrange(1, T + 1):
    J, P, S, K = map(int, raw_input().split())
    jps = set()
    jp = coll.defaultdict(int)
    js = coll.defaultdict(int)
    ps = coll.defaultdict(int)
    ans = []
    p, s = 1, 1
    for j in xrange(1, J + 1):
        for loop in xrange(10000):
            if (j, p, s) in jps: continue
            if jp[(j, p)] < K and js[(j, s)] < K and ps[(p, s)] < K:
                ans.append((j, p, s))
                jp[(j, p)] += 1
                js[(j, s)] += 1
                ps[(p, s)] += 1
                jps.add((j, p, s))
            p = (p + 7) % P + 1
            s = (s + 13) % S + 1
    print "Case #%d: %d" % (case, len(ans))
    for j, p, s in jps:
        print j, p, s
