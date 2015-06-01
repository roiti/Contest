import itertools
while 1:
    n,k,s = map(int,raw_input().split())
    if n == 0: break
    print sum(sum(ele) == s for ele in itertools.combinations(range(1,n+1),k))

