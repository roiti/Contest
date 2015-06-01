while 1:
    N = int(raw_input())
    if N == 0: break
    W,H = map(int,raw_input().split())
    A = [[0]*W for _ in range(H)]
    for i in range(N):
        w,h = map(int,raw_input().split())
        A[h-1][w-1] = 1
    S,T = map(int,raw_input().split())
    S,T = S,T
    
    ans = 0
    for h in range(H-T+1):
        for w in range(W-S+1):
            ans = max(ans, sum(sum(A[h+i][w:w+S]) for i in range(T)))
    print ans

