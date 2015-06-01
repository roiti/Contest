while 1:
    N = int(raw_input())
    if N == 0: break
    free = [map(int,raw_input().split())[1:] for i in xrange(N)]
    have = [set([i]) for i in xrange(N)]
    for day in xrange(1,31):
        gather = set([])
        come = [i for i in xrange(N) if day in free[i]]
        for i in come:
            gather |= have[i]
        if len(gather) == N:
            print day
            break
        for i in come:
            have[i] = gather.copy()
    else:
        print -1
    


