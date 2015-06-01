while 1:
    n = int(raw_input())
    if n == 0: break
    S = [list(raw_input()) for i in xrange(n)]

    for y in xrange(n):
        for x in range(len(S[y])):     
            if S[y][x] == ".": S[y][x] = " "
            else:
                if x > 0:
                    S[y][x-1] = "+"
                    t = y-1
                    while S[t][x-1] == " ":
                        S[t][x-1] = "|"
                        t -= 1
                break
    for s in S: print "".join(s)


