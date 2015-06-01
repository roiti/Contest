Q = int(raw_input())
for loop in xrange(Q):
    N, T = map(int, raw_input().split())
    for i in xrange(T):
        if N % 2 == 0:
            N -= N / 2
        else:
            N -= (N + 1) / 2
        N -= N / 4
    print N
