T = int(raw_input())
for case in xrange(1, T + 1):
    B, N = map(int, raw_input().split())
    M = map(int, raw_input().split())
    l, r = 0, 10 ** 15

    m = N
    for i in xrange(50):
        t = (l + r) / 2
        n = sum(t / M[i] + 1 for i in xrange(B))
        if n >= N:
            r = t
        else:
            l = t

    N -= (n - 1)
    for i in xrange(B):
        if (t + 1) % M[i] == 0:
            N -= 1
            if N == 0:
                ans = i + 1
                break
    print "Case #%d: %d"%(case, ans)
