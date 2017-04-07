N, T = map(int, raw_input().split())
A = map(int, raw_input().split())

X = [0]*N
for i in xrange(N - 2, -1, -1):
    X[i] = max(X[i + 1], A[i + 1])

mx, cnt = 0, 0
for i, a in enumerate(A):
    tmp = X[i]
    if tmp - a > mx:
        mx = tmp - a
	cnt = 1
    elif tmp - a == mx:
        cnt += 1
print cnt
