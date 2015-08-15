N,M = map(int,raw_input().split())
AB = [map(int,raw_input().split()) for _ in range(M)]
high = set([])
for a,b in AB:
    if b == 1: high.add(a)
while 1:
    adds = set([])
    flag = False
    for i in high:
        for a,b in AB:
            if b == i and a not in high:
                adds.add(a)
                flag = True
    if flag == False: break
    high |= adds
print len(high)+1
