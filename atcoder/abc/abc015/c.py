import itertools
N,K = map(int,raw_input().split())
T = [map(int,raw_input().split()) for i in range(N)]
for ls in itertools.product(range(K),repeat=N):
    ans = reduce(lambda a,b:a^b, [T[i][ls[i]] for i in range(N)])
    if ans == 0:
        print "Found"
        break
else:
    print "Nothing"
