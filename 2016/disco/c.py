# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
N = len(S)
K = int(raw_input())

z = 0
T = ""
for i in xrange(N):
    if S[i] == "a":
        T += "a"
    else:
        if K > 0:
            T += S[i].upper() 
            K -= 1
            z += 1
        else:
            T += S[i]

flag = True
for t in T:
    if t.islower() and t != "a":
        flag = False

if flag:
    ans = "".join(t for t in T if t == "a")
    ans = ans[:len(ans) - K]
else:
    ans = ""
    f = False
    for t in T[::-1]:
        if t.isupper():
            if not f:
                z -= 1
                continue
            else:
                if z > 1:
                    ans += "a"
                    z -= 1
                else:
                    if ans[-1] < t.lower():
                        ans += "a"
                    else:
                        ans += t.lower() + "a"
        else:
            if t != "a": f = True
            ans += t
    ans = ans[::-1]
print ans
