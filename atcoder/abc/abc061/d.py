# -*- coding: utf-8 -*-
inf = float('inf')
N, M = map(int, raw_input().split())
abc = [map(int, raw_input().split()) for i in xrange(M)]
abc = [[a - 1, b - 1, c] for a, b, c in abc]

def find_negative_loop():
    d = [0]*N
    for i in xrange(N):
        for a, b, c in abc:
            if d[b] > d[a] - c:
                d[b] = d[a] - c
                if i == N - 1: return True
    return False

def bellman_ford(s):
    d = [inf]*N
    d[s] = 0
    while True:
        update = False
        for a, b, c in abc:
            if d[a] != inf and d[b] > d[a] - c:
                d[b] = d[a] - c
                update = True
        if not update:
            break
    return d

if find_negative_loop():
    print 'inf'
else:
    d = bellman_ford(0)
    print -d[N - 1]
