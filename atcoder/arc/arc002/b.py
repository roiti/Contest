day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Y, M, D = map(int, raw_input().split(/))
while 1:
    if Y % M == 0 and Y / M % D == 0:
        print "%s/%02d/%02d" % (Y, M, D)
        break
    if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
        day[1] = 29
    else:
        day[1] = 28
    D += 1
    if D > day[M - 1]:
        D = 1
        M += 1
        if M > 12:
            M = 1
            Y += 1

