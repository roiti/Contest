# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"

s = raw_input()
K = int(raw_input())
dic = dict([alpha[i], i] for i in xrange(len(alpha)))

ans = [] 
for si in s:
    d = 26 - dic[si] if si != "a" else 0
    if d <= K:
        ans.append("a")
        K -= d
    else:
        ans.append(si)

if K > 0:
    ans[-1] = alpha[(dic[ans[-1]] + K) % 26]

print "".join(ans)
