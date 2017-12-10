def solve():
    N, M, K = map(int, raw_input().split()) 

    for i in xrange(N + 1):
        cur = M*i
        if cur > K: break
        for j in xrange(M + 1):
            if cur - i*j + (N - i)*j == K:
                return True
    for i in xrange(M + 1):
        cur = N*i
        if cur > K: break
        for j in xrange(N + 1):
            if cur - i*j + (M - i)*j == K:
                return True

    return False

print "Yes" if solve() else "No"
