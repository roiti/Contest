A, B, C, K = map(int, raw_input().split())
S, T = map(int, raw_input().split())
ans = A * S + B * T
if S + T  >= K:
    ans -= C * (S + T)
print ans
