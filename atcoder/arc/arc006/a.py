E = set(raw_input().split())
B = raw_input()
L = set(raw_input().split())

cnt = len(E & L)
bonus = B in (L - E)

if   cnt == 6: print 1
elif cnt == 5:
    if bonus: print 2
    else: print 3
elif cnt == 4:
    print 4
elif cnt == 3:
    print 5
else:
    print 0
