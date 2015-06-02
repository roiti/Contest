while True:
    h, w = map(int, raw_input().split())

    if h == 0 and w == 0:
        break

    for i in range(0, h):
        wid = ""
        for j in range(0, w):
            wid += "#"
        print wid
    print ""


