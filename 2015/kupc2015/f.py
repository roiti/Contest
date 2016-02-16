# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def solve(s):
    X = []
    B = []
    T = []
    for i in xrange(len(s)):
        if s[i].isdigit():
            X.append((s[i], True))
        else:
            r, f1 = X.pop()
            l, f2 = X.pop()
            X.append((str(eval("%s%s(%s)" % (l, s[i], r))), False))
            if f1: B.append(r)
            if f2: B.append(l)
            T.append(s[i])
    return "".join(B)[::-1] + "".join(T)

def calc1(s):
    X = []
    for i in xrange(len(s)):
        if s[i].isdigit():
            X.append(s[i])
        else:
            r = X.pop()
            l = X.pop()
            X.append(str(eval("%s%s(%s)" % (l, s[i], r))))
        print X
    return X[0]

def calc2(s):
    X = []
    for i in xrange(len(s)):
        if s[i].isdigit():
            X.append(s[i])
        else:
            r = X.pop(0)
            l = X.pop(0)
            X.append(str(eval("%s%s(%s)" % (l, s[i], r))))
        print X
    return X[0]


A = raw_input()
B = solve(A) if len(A) > 1 else A
print B
print calc1(A), calc2(B)
