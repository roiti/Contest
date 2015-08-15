N,T = map(int,raw_input().split())
A = [int(raw_input()) for _ in range(N)]
ans = 0
for t in range(1,T+1):
    tmp = sum(1 for i in range(N) if t%A[i] == 0)
    ans = max(ans,tmp)
print ans
