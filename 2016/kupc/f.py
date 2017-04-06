# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def solve(f):
    global i, r0, r1
    l, r = "", ""
    left = True
    while s[i] != "?":
        if s[i] == ",":
            i += 1
            left = False
            continue
        if s[i] == ")":
            i += 1
            return max(int(l), int(r)) if f == "^" else min(int(l), int(r))

        if left:
            if s[i] in ["^", "_"]:
                nf = s[i]
                i += 2
                l = solve(nf)
                left = False
            else:
                l += s[i]
                if f == "_" and l == "0":
                    return 0
                if f == "^" and l == "99":
                    return 99
                i += 1
        else:
            if s[i] in ["^", "_"]:
                nf = s[i]
                i += 2
                return max(int(l), solve(nf)) if f == "^" else min(int(l), solve(nf))
            else:
                r += s[i]
                if f == "_" and r == "0":
                    return 0
                if f == "_" and min(int(l), int(r)) == int(l):
                    return int(l) 
                if f == "^" and max(int(l), int(r + "9")) == int(l):
                    return int(l) 
                i += 1
    
Q = int(raw_input())
for loop in xrange(Q):
    s = raw_input()
    if s[0] != "_" and s[0] != "^":
        print s[:-1], len(s)
    else:
        i = 2
        print solve(s[0]), i if s[i] == ")" else i + 1, s[i]

