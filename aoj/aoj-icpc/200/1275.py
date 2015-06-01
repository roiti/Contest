while 1:
    n,k,m = map(int,raw_input().split())
    if n == 0: break
    stone = range(1,n+1)
    p = m-1
    while len(stone) > 1:
        stone.pop(p)
        p = (p+k-1)%len(stone)
    print stone[0]


