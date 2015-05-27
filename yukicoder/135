N = int(raw_input())
X = sorted(list(set(map(int,raw_input().split()))))
if len(X) == 1:
    print 0
else:
    ans = 10**10
    for i in range(len(X)-1):
        ans = min(ans, X[i+1]-X[i])
    print ans