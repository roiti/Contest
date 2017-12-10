# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for case in xrange(1, T + 1):
    J, P, S, K = map(int, raw_input().split())

    ans = 0
    ans_set = set()
    now = set()
    for j in xrange(1, J + 1):
        for p in xrange(1, P + 1):
            for s in xrange(1, S + 1):
                now.add(frozenset(((j, p, s),)))

    for loop in xrange(J*P*S):
        nxt = set()
        for jpss in now:
            if len(jpss) > ans:
                ans = len(jpss)
                ans_set = jpss
            for j in xrange(1, J + 1):
                for p in xrange(1, P + 1):
                    for s in xrange(1, S + 1):
                        if (j, p, s) in jpss: continue
                        jp = coll.defaultdict(int)
                        js = coll.defaultdict(int)
                        ps = coll.defaultdict(int)
                        jp[(j, p)] += 1
                        js[(j, s)] += 1
                        ps[(p, s)] += 1
                        for jj, pp, ss in jpss:
                            jp[(jj, pp)] += 1
                            js[(jj, ss)] += 1
                            ps[(pp, ss)] += 1
                        if max(v for v in jp.values()) <= K and max(v for v in js.values()) <= K and max(v for v in ps.values()) <= K:
                            n_jpss = frozenset(jpss | frozenset(((j, p, s),)))
                            nxt.add(n_jpss)
        now = nxt
    print "Case #%d: %d" % (case, ans)
    for j, p, s in ans_set:
        print j, p, s
