while True:
    h, w = map(int, raw_input().split())

    if h == 0 and w == 0:
        break
    
    hcnt = 1
    for i in range(0, h):
        wid = ""
        if hcnt == 1 or hcnt == h:
            for j in range(0, w):
                wid += "#"
            print wid
        else:
            wid += "#"
            for j in range(1, w-1):
                wid += "."
            wid += "#"
            print wid
        hcnt += 1
    print ""

