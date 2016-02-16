# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

p = [1] * 1001
p[0] = p[1] = 0
for i in xrange(2, 36):
    if p[i]:
        p[2*i::i] = [0] * len(p[2*i::i])
prime = []
for i in xrange(1001):
    if p[i]:
        prime.append(i)
ans = 1
for n in prime:
    m = 1
    while m * n <= 1000:
        print "?", m * n
        sys.stdout.flush()
        res = raw_input()
        if res == "N":
            break
        m *= n
    ans *= m
    if ans * n > 1000:
        break
print "!", ans
