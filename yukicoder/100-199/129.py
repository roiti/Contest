import sys
sys.setrecursionlimit(10000)
def perm(n,i):
    return 1 if i == 0 else n*perm(n-1,i-1)

N = int(raw_input())
M = int(raw_input())

R = (N-N/1000/M*1000*M)/1000
R = min(R,M-R)
print perm(M,R)/perm(R,R)%10**9