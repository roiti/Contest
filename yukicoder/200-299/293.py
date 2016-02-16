# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A, B = raw_input().split()
if len(A) > len(B):
    print A
elif len(A) < len(B):
    print B
else:
    for i, j in zip(A, B):
        if i not in ["4", "7"] or j not in ["4", "7"]:
            if int(i) > int(j):
                print A
                break
            elif int(i) < int(j):
                print B
                break
        else:
            if i == "4" and j == "7":
                print A
                break
            elif i == "7" and j == "4":
                print B
                break

