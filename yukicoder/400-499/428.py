# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

D = 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495969798991
N = int(raw_input())
D = str(D*N)

if len(D) == 190:
    print "0." + D
elif len(D) == 191:
    print D[0] + "." + D[1:]
elif len(D) == 192:
    print D[:2] + "." + D[2:]
else:
    print D[:3] + "." + D[3:]
