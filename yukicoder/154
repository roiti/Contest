T = int(raw_input())
for loop in xrange(T):
    S = raw_input()
    w = last = cnt = 0
    needG = False
    for s in S:
        if   s == "G":
            last += 1
            w -= 1
            needG = False
        elif s == "R":
            last -= 1
        else:
            w += 1
            needG = True
        if last < 0 or w < 0:
            print "impossible"
            break
    else:
        print "possible" if last == 0 and not needG else "impossible"
