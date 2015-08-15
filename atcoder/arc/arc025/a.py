J = map(int, raw_input().split())
D = map(int, raw_input().split())
print sum(max(i, j) for i, j in zip(J, D))
