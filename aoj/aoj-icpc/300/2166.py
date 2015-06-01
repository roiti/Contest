INF = 10**10
def rec(cur, cycle):
    if   dp[cur][cycle] > -1: pass
    elif cur == 100: dp[cur][cycle] = 0
    elif until[cur] < t[cycle]: dp[cur][cycle] = INF
    else: dp[cur][cycle] = min(rec(cur+1, (cycle+1)%T), 1+rec(cur+1, 0))
    return dp[cur][cycle]
    
while 1:
    T = int(raw_input())
    if T == 0: break
    t = map(int,raw_input().split())
    N = int(raw_input())
    until = [INF]*100
    for loop in xrange(N):
        D,M = map(int,raw_input().split())
        until[D-1] = min(until[D-1], M)
    
    dp = [[-1]*33 for i in xrange(101)]
    print rec(0,0)


