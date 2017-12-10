# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for case in xrange(T):
    N = int(raw_input())
    S = [raw_input().split() for i in xrange(N)]
    cnt1 = coll.defaultdict(int)
    cnt2 = coll.defaultdict(int)
    for x, y in S:
        cnt1[x] += 1
        cnt2[y] += 1

    whole = set(range(N))
    original = set()
    for i, s in enumerate(S):
        if cnt1[s[0]] == 1:
            original.add(i)
        if cnt2[s[1]] == 1:
            original.add(i)

    cand = whole - original
    first = set()
    second = set()
    ans = 0
    for i in cand:
        if S[i][0] in first or S[i][1] in second:
            ans += 1
        else:
            first.add(S[i][0])
            second.add(S[i][1])

    print "Case #%d: %d" % (case + 1, ans)
