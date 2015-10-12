# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

dic = []
for i in xrange(1, 10):
    tmp = []
    for ele in it.product("47", repeat = i):
        tmp.append("".join(ele))
    tmp.sort()
    dic += tmp

n = raw_input()
print dic.index(n) + 1
