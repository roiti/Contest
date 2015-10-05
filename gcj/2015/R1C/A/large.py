T = int(raw_input())        
for case in xrange(1, T + 1):
    R, C, W = map(int, raw_input().split())
    ans = C / W * (R - 1) + (C / W + W - 1 + min(1, C % W))
    print "Case #%d: %d" % (case, ans)
