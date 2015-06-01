while 1:
    N,M = map(int,raw_input().split())
    if N == M == 0: break
    DP = [map(int,raw_input().split()) for _ in xrange(N)]
    DP = sorted(DP, key = lambda x:x[1], reverse = True)

    ans = 0
    for i in xrange(N):
        if M-DP[i][0] >= 0:
            M -= DP[i][0]
        else:
            ans += DP[i][1]*(DP[i][0]-M)
            ans += sum(DP[j][1]*DP[j][0] for j in xrange(i+1,N))
            break
    print ans

