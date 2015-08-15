def divide(n):
    res = 1
    i = 2
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n /= i
            cnt += 1
        if cnt > 0:
            res *= sum(i ** j for j in xrange(cnt + 1))
        i += 1
    if n > 1:
        res *= 1 + n
    return res

N = int(raw_input())
v = divide(N) - N
print "Perfect" if v == N else "Deficient" if v < N else "Abundant"
