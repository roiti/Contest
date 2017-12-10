# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for case in xrange(1, T + 1):
    J, P, S, K = map(int, raw_input().split())

    ans = 0
    ans_set = set()
    all_comb = [(j, p, s) for j in xrange(1, J + 1) for p in xrange(1, P + 1) for s in xrange(1, S + 1)]
    flag = False
    for ans in xrange(J*P*S, 0, -1):
        for choose in it.combinations(all_comb, ans):
            jp = coll.defaultdict(int)
            js = coll.defaultdict(int)
            ps = coll.defaultdict(int)
            for j, p, s in choose:
                jp[(j, p)] += 1
                js[(j, s)] += 1
                ps[(p, s)] += 1

            if max(v for v in jp.values()) <= K and max(v for v in js.values()) <= K and max(v for v in ps.values()) <= K:
                print "Case #%d: %d" % (case, len(choose))
                for j, p, s in choose:
                    print j, p, s
                flag = True
                break
        if flag:
            break
