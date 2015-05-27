N = int(raw_input())
M = int(raw_input())
cup = range(3)
for loop in range(M):
    p,q = map(int,raw_input().split())
    p -= 1; q -= 1
    cup[p],cup[q] = cup[q],cup[p]
print cup.index(N-1)+1