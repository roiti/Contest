m, n, N = map(int, raw_input().split())
ans = 0
rmn = 0
while N > 0:
    while N > 0:
        ans += N
        rmn += N % m
        N = N / m * n
        N = rmn / m * n
        rmn = rmn % m
print ans
