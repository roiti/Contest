from collections import defaultdict
while 1:
    n = int(raw_input())
    if n == 0: break
    L = [0]*n
    T = [0]*n
    for man in xrange(n):
        m,l = map(int,raw_input().split())
        L[man] = l
        t = 0
        for date in xrange(m):
            s,e = map(int,raw_input().split())
            t |= 2**(e-6)-2**(s-6)
        T[man] = t

    dp = defaultdict(int)
    for l,t in zip(L,T):
        for bit in dp.keys():
            if bit&t == 0:
                dp[bit|t] = max(dp[bit|t], dp[bit]+l)
        dp[t] = max(dp[t], l)
        
    print max(dp.values())


