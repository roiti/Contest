import itertools as it
N = int(raw_input())
A = map(int,raw_input().split())
M = int(raw_input())
_B = sorted(map(int,raw_input().split()),reverse = True)
ans = M+1
for order in it.permutations(A,N):
    B = _B[:]
    i = j = 0
    while i < N and j < M:
        if B[j] >= order[i]:
            B[j] -= order[i]
            i += 1
        else:
            j += 1
    ans = min(ans, j+1)
print ans if ans < M+1 else -1
    
