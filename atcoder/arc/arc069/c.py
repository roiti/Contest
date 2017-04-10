N, M = map(int, raw_input().split())
ans = min(N, M/2)
M -= 2*ans
ans += M/4
print ans
