n = int(raw_input())
for loop in range(n):
    l,r = map(int,raw_input().split())
    i = 0
    while 1:
        if l|1<<i <= r: l |= 1<<i
        else: break
        i += 1
    print l
