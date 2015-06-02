n, _k = map(int, raw_input().split())
w = [int(raw_input()) for i in xrange(n)]

l, r = max(w), sum(w)
while r > l:
    P = (r + l) / 2
    c = P
    k = _k - 1
    for wi in w:
        if c >= wi: c -= wi
        else:
            c = P - wi
            k -= 1
            if k < 0:
                break
    if k >= 0:
        r = P
    else:
        l = P + 1
print l
