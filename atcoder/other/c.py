ans = [0] * 200005
for i in xrange(1, 200001):
    mx = max(int(j) for j in str(i))
    ans[i] = ans[i - mx] + 1

Q = int(raw_input())
for query in xrange(Q):
    N = int(raw_input())
    print ans[N]


