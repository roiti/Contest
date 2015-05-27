N = int(raw_input())
A = map(int,raw_input().split())+[0]*1000
ans = 1e10
for n in range(1,10001,2):
    P = [min(i,n+1-i) for i in range(1,n+1)]
    if sum(P) > sum(A): break
    for j in range(N):
        over = lack = 0
        for k in range(n):
            tmp = A[j+k]-P[k]
            if tmp > 0: over += tmp
            else: lack += abs(tmp)
        ans = min(ans, min(over,lack)+max(0,over-lack)+sum(A)-sum(A[j:j+n]))
print ans