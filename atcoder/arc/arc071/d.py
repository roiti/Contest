# -*- coding: utf-8 -*-
S = raw_input()
T = raw_input()
 
N, M = len(S), len(T)
SA, SB = [0]*(N + 2), [0]*(N + 1)
TA, TB = [0]*(M + 1), [0]*(M + 1)
for i in xrange(1, N + 1):
    SA[i] = SA[i - 1] + (1 if S[i - 1] == "A" else 0)
    SB[i] = SB[i - 1] + (1 if S[i - 1] == "B" else 0)
for i in xrange(1, M + 1):
    TA[i] = TA[i - 1] + (1 if T[i - 1] == "A" else 0)
    TB[i] = TB[i - 1] + (1 if T[i - 1] == "B" else 0)
 
q = int(raw_input())
for loop  in xrange(q):
    a, b, c, d = map(int, raw_input().split())
    A0 = SA[b] - SA[a - 1]
    B0 = SB[b] - SB[a - 1]
    A1 = TA[d] - TA[c - 1]
    B1 = TB[d] - TB[c - 1]
    A0 += 2*B0
    A1 += 2*B1
    A0 %= 3
    A1 %= 3
 
    if A0 == A1:
        print "YES"
    else:
        print "NO"
