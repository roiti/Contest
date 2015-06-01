while 1:
    n,w,d = map(int,raw_input().split())
    if w == 0: break
    cake = [[w,d]]
    for loop in xrange(n):
        p,s = map(int,raw_input().split())
        x,y = cake.pop(p-1)
        s %= (x+y)
        if s < x:
            x1,x2 = sorted([s,x-s])
            cake += [[x1,y],[x2,y]]
        else:
            s -= x
            y1,y2 = sorted([s,y-s])
            cake += [[x,y1],[x,y2]]
    print " ".join(map(str,sorted([x*y for x,y in cake])))


