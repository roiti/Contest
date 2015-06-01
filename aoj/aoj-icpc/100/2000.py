while True:
    n = int(raw_input())
    if n == 0:
        break
    f = [[0 for i in range(21)] for i in range(21)]
    for i in range(n):
        x, y = map(int, raw_input().split())
        f[y][x] = 1

    n = int(raw_input())
    x,y = 10, 10
    for i in range(n):
        c, d = map(str, raw_input().split())
        d = int(d)
        if c == "N":
            for j in range(1,d+1):
                f[y+j][x] = 0
            y += d
        elif c == "E":
            for j in range(1,d+1):
                f[y][x+j] = 0
            x += d
        elif c == "S":
            for j in range(1,d+1):
                f[y-j][x] = 0
            y -= d
        else:
            for j in range(1,d+1):
                f[y][x-j] = 0
            x -= d
    for i in range(20):
        if 1 in f[i][:]:
            print "No"
            break
        if i == 19:
            print "Yes"

