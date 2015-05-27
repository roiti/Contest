mod = 10**9+7
def mul(A, B):
    C = [[0]*2 for _ in range(2)]
    C[0][0] = (A[0][0]*B[0][0]+A[0][1]*B[1][0])%mod
    C[0][1] = (A[0][0]*B[1][0]+A[0][1]*B[1][1])%mod
    C[1][0] = (A[1][0]*B[0][0]+A[1][1]*B[1][0])%mod
    C[1][1] = (A[1][0]*B[1][0]+A[1][1]*B[1][1])%mod
    return C

def mat_pow(A, n):
    B = [[1,0],[0,1]]
    while n:
        if n & 1: B = mul(A, B)
        A = mul(A, A)
        n >>= 1
    return B

def pow_mod(a,p,mod):
    if p == 0: return 0
    res = 1
    while p:
        if p & 1: res = (res*a)%mod
        a = a*a%mod
        p >>= 1
    return res
    
N = int(raw_input())
ans = 1
for loop in range(N):
    c,d = map(int,raw_input().split())
    A = [[1,1],[1,0]]
    comb = mat_pow(A,c+2)[1][0]
    while d > mod-1:
        d %= mod-1
    ans = ans*pow_mod(comb,d,mod)%mod
print ans