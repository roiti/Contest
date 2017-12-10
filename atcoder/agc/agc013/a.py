# -*- coding: utf-8 -*-

N = int(raw_input())
A = map(int, raw_input().split())
B = [A[0]]
for ai in A[1:]:
    if B[-1] != ai:
        B.append(ai)
A = B[:]
N  = len(A)

ans = 1
i = 0
while i < N - 2:
    if A[i] <= A[i + 1] <= A[i + 2]:
        i += 1
    elif A[i] >= A[i + 1] >= A[i + 2]:
        i += 1
    else:
        ans += 1
        i += 2

print ans
