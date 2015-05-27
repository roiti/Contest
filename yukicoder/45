N = int(raw_input())
if N == 1: print int(raw_input())
else:
    V = map(int,raw_input().split())
    dp = [0]*N
    dp[0] = V[0]
    dp[1] = max(V[0],V[1])
    for i in range(2,N):
        dp[i] = max(dp[i-1],dp[i-2]+V[i])
    print dp[N-1]