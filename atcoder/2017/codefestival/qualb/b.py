# -*- coding: utf-8 -*-
from collections import defaultdict

def solve():
    N = int(raw_input())
    D = map(int, raw_input().split())
    cnt = defaultdict(int)
    for di in D:
        cnt[di] += 1
    M = int(raw_input())
    T = map(int, raw_input().split())
    for ti in T:
        if cnt[ti] == 0:
            return False
        cnt[ti] -= 1
    return True

print "YES" if solve() else "NO"
