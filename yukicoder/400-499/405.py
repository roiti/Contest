# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

ref = ["I","II","III","IIII","V","VI","VII","VIII","IX","X","XI","XII"]
S1, T = raw_input().split()
print ref[(ref.index(S1) + int(T))%12]
