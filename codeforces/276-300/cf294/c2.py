n,m = map(int,raw_input().split())
ans = 0
while n and m:
    if max(n,m) == 1: break
    if n > m:
        n -= 2
        m -= 1
    else:
        n -= 1
        m -= 2
    ans += 1
print ans
