N,M = map(int,raw_input().split())
C = sorted(map(int,raw_input().split()))
ans = 0
for i in xrange(N):
    if M >= C[i]:
        ans += 1
        M -= C[i]
print ans
