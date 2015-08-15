N = int(raw_input())
V = map(int,raw_input().split())
F = map(int,raw_input().split())
print sum(1 for i in range(N) if 2*F[i] > V[i])
