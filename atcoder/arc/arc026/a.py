N, A, B = map(int, raw_input().split())
print min(N, 5) * B + max(0, N - 5) * A
