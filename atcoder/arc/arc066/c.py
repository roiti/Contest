mod = 10**9 + 7

N = int(raw_input())
A = map(int, raw_input().split())
A.sort(reverse = True)

ans = 1
for i in xrange(N/2):
    if A[2*i] == A[2*i + 1] == abs((N - 1 - i) - i):
        pass
    else:
        ans = 0
if ans:
    ans = pow(2, N/2, mod)
print ans
