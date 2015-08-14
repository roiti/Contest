import itertools
N,M = map(int,raw_input().split())
chain = [set([i]) for i in xrange(N)]
for loop in xrange(M):
    a,b = map(int,raw_input().split())
    chain[a-1].add(b-1)
    chain[b-1].add(a-1)
ans = 1    
for comb in itertools.product([0,1],repeat=N):
    if comb.count(1) < 2: continue
    group = reduce(lambda a,b: a&b, [chain[i] for i in xrange(N) if comb[i]])
    for i in xrange(N):
        if comb[i] and i not in group:
            break
    else:
        ans = max(ans, comb.count(1))
print ans
