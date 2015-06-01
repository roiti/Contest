n = int(raw_input())
for loop in xrange(n):
    a = []
    while len(a) < 9:
        a += map(lambda i:int(i,16),raw_input().split())
    key = 0
    for i in xrange(32):
        s = sum(a[j]^key for j in xrange(8))
        if (s^a[-1]^key) & (1 << (i+1)-1) != 0: key |= (1 << i)
    print "%x"%key

