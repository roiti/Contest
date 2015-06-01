while 1:
    N,T,L,B = map(int,raw_input().split())
    if N == 0: break
    lose = set([int(raw_input()) for i in xrange(L)])
    back = set([int(raw_input()) for i in xrange(B)])
    dp = [[0.]*(N+1) for i in xrange(T+1)]
    dp[0][0] = 1.
    p = 1./6.
    for t in xrange(T):
        for i in xrange(N):
            tt = t-1 if i in lose else t
            for j in xrange(i+1,i+7):
                if j > N: j = N-j%N
                if j in back: j = 0
                dp[t+1][j] += p*dp[tt][i]
        dp[t+1][N] += dp[t][N]
    print "%.6f"%dp[T][N]

