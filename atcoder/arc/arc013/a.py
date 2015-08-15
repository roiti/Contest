import itertools as it
N, M, L = map(int, raw_input().split())
P, Q, R = map(int, raw_input().split())
print max((N / p) * (M / q) * (L / r) for p, q, r in it.permutations([P, Q, R], 3))
