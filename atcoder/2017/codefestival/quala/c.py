# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def solve():
    H, W = map(int, raw_input().split())
    a = [list(raw_input()) for i in xrange(H)]

    cnt = [0]*26
    for ai in a:
        for c in ai:
            cnt[ord(c) - ord("a")] += 1
    if H%2 == 0 and W%2 == 0:
        for i in xrange(26):
            if cnt[i]%4 != 0:
                return False
        return True
    elif H%2 == 0 or W%2 == 0:
        for i in xrange(26):
            if cnt[i]%2 != 0:
                return False
            cnt[i] /= 2
        X = W/2 if W%2 == 0 else H/2
        odd = sum(cnt[i]%2 != 0 for i in xrange(26)) 
        return odd <= X 
    else:
        odd = sum(cnt[i]%2 != 0 for i in xrange(26)) 
        four = sum(cnt[i]/4 for i in xrange(26))
        return odd == 1 and four >= (H/2)*(W/2)

print "Yes" if solve() else "No"
