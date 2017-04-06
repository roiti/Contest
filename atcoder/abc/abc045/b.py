# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

SA = raw_input()
SB = raw_input()
SC = raw_input()

x = SA[0]
SA = SA[1:]
while 1:
    if x == "a" and SA:
        x = SA[0]
        SA = SA[1:]
    elif x == "b" and SB:
        x = SB[0]
        SB = SB[1:]
    elif x == "c" and SC:
        x = SC[0]
        SC = SC[1:]
    else:
        print x.upper()
        break
