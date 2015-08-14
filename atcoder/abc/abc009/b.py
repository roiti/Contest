n = int(raw_input())
A = sorted(list(set([int(raw_input()) for _ in range(n)])))
print A[-2]
