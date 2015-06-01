while 1:
    w,d = map(int,raw_input().split())
    if w == 0: break
    front = map(int,raw_input().split())
    side = map(int,raw_input().split())
    for i in front:
        if i in side: side.remove(i)
    ans = sum(front)+sum(side)
    print ans


