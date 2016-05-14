# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

cand = [0]*4
mx = 0
while 1:
    for Ms in it.combinations(cand, mx):
        flag = False
        for Ns in it.combinations(set(range(10)) - set(cand), 4 - len(cand)):
            print " ".join(map(str, Ms + Ns))
            sys.stdout.flush()
            X, Y = map(int, raw_input().split())
            if X + Y > mx:
                mx = X + Y
                cand = Ms + Ns
                flag = True
                break
        if flag:
            break
    if mx == 4:
        break

for Ns in it.permutations(cand, 4):
    print " ".join(map(str, Ns))
    sys.stdout.flush()
    X, Y = map(int, raw_input().split())
    if X == 4:
        break

