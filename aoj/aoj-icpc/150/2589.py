while 1:
    s = raw_input().replace("north","0").replace("west","1")[::-1]
    if s == "#": break
    u = 90*int(s[0])
    s = s[1:]
    d = 2**len(s)
    for i in s:
        u = 2*u+(90 if i == "1" else -90)
    while u%2 == 0 and d > 1:
        u /= 2; d /= 2
    print u if d == 1 else "%d/%d"%(u,d)

