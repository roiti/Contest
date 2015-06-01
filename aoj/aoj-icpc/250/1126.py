while 1:
    W,H = map(int,raw_input().split())
    if W == 0: break
    C = [list(raw_input()) for _ in xrange(H)]
    dp = [[0]*W for _ in xrange(H)]
    ans = 0
    for h in xrange(H):
        for w in xrange(W):
            if C[h][w].isdigit():
                dp[h][w] = max(dp[h][w],int(C[h][w]))
                if w > 0: dp[h][w] = max(dp[h][w],int(str(dp[h][w-1])+C[h][w]))
                if h > 0: dp[h][w] = max(dp[h][w],int(str(dp[h-1][w])+C[h][w]))
    print max(max(i) for i in dp)


