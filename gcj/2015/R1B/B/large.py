T = int(raw_input())
for case in xrange(1, T + 1):
    R, C, N = map(int, raw_input().split())
    if min(R, C) == 1:
        X = max(R, C)
        ans = max(0, 2 * (N - (X + 1) / 2))
        if X % 2 == 0: ans = max(0, ans - 1)
        print "Case #%d: %d" % (case, ans)
        continue
    
    ans = 0
    if R % 2 + C % 2 == 2:
        if N <= (R * C / 2 + 1) + 2:
            ans = 3 * max(0, N - (R * C / 2 + 1))
        else:
            silent = R * C / 2
            N -= silent
            ans += min(4 * 2, max(0, 4 * N))
            N -= 4
            noisy = max(0, (R - 2) * (C - 2) / 2)
            soso = silent - 4 - noisy
            ans += min(3 * soso, max(0, 3 * N))
            N -= soso
            ans += max(0, 4 * N)
        
    if R % 2 + C % 2 < 2:
        silent = R * C / 2
        N -= silent
        ans += min(2 * 2, max(0, 2 * N))
        N -= 2
        noisy = max(0, (R - 2) * (C - 2) / 2)
        soso = silent - 2 - noisy
        ans += min(3 * soso, max(0, 3 * N))
        N -= soso
        ans += max(0, 4 * N)
        
    print "Case #%d: %d" % (case, ans)
