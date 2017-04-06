# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def med(a):
    return sorted(a)[1]

def simu(a):
    while len(a) > 1:
        a = [med([a[i], a[i + 1], a[i + 2]]) for i in xrange(len(a) - 2)]
    return a[0]

#for ele in it.permutations(xrange(1, 8)):
#    if simu(ele) == 2:
#        print ele

N, x = map(int, raw_input().split())
d = x - N
if 1 < x <= 2*N - 2:
    print "Yes"
    ans = [(i + d)%(2*N - 1) + 1 for i in xrange(2*N - 1)]
    print "\n".join(map(str, ans))
    #print simu(ans)
else:
    print "No"
