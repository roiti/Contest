N, B, C = map(int, raw_input().split())
A = sorted(map(int, raw_input().split()), reverse = True)

ans = 0
for Ai in A:
    x = min(C, B)
    ans += Ai * x
    C -= x
print ans
