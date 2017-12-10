# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
words = [raw_input() for i in xrange(N)]

for i in xrange(N):
    for j in xrange(N):
        if i == j: continue
        cnt = 0
        for x, y in zip(words[i], words[j]):
            if x != y:
                cnt += 1
        if cnt > 1:
            flag = False
            break
    else:
        print words[i]
        exit()
