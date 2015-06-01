dwh = zip([1,1,0,-1,-1,-1,0,1],[0,1,1,1,0,-1,-1,-1])
while 1:
    H,W = map(int,raw_input().split())
    if H == 0: break
    S = [raw_input() for i in xrange(H)]
    
    ans = ""
    appear = set([])
    for h in xrange(H):
        for w in xrange(W):
            for dw,dh in dwh:
                s = S[h][w]
                iw,ih = w,h
                w = (w+dw+W)%W; h = (h+dh+H)%H
                while (w,h) != (iw,ih):
                    s += S[h][w]
                    if s in appear:
                        if len(s)  > len(ans): ans = s
                        if len(s) == len(ans): ans = min(ans, s)
                    appear.add(s)
                    w = (w+dw+W)%W; h = (h+dh+H)%H
    print ans if len(ans) > 1 else 0


