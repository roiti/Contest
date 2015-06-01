while 1:
    n = int(raw_input())
    if n == 0: break
    ab = [raw_input().split() for i in xrange(n)]
    s = raw_input()
    g = raw_input()
    memo = set([s])
    que = [[s,0]]
    while que:
        c,i = que.pop(0)
        if c == g:
            print i
            break
        for a,b in ab:
            cc = c.replace(a,b)
            if len(cc) > len(g) or cc in memo: continue
            memo.add(cc)
            que.append([cc,i+1])
    else:
        print -1


