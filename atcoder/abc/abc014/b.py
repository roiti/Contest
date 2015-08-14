n,X = map(int,raw_input().split())
a = map(int,raw_input().split())
ans = 0
for bit in range(n):
    if X&1: ans += a[bit]
    X /= 2
print ans
