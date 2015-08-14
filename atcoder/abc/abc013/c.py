N,H = map(int,raw_input().split())
A,B,C,D,E = map(int,raw_input().split())
ans = A*N
for I in range(N+1):
    J = ((N-I)*E-H-I*B)/(D+E)+1
    ans = min(ans,I*A+max(0,J*C))
print ans
