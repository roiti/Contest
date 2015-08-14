import math,string,random,itertools,bisect
inf = 0x10101010
pi = math.pi
# Functions
########################################################
 
 
# main procedure
########################################################
N = int(raw_input())
R = map(int,raw_input().split())
S = [R[0]]
for r in R:
    if S[-1] != r:
        S.append(r)
R = S[:]
N = len(R)
ans = [R[0]]
for i in range(1,N-1):
    if (R[i-1] > R[i] < R[i+1]) or (R[i-1] < R[i] > R[i+1]):
        ans.append(R[i])
ans.append(R[-1])
print len(ans) if len(ans) > 2 else 0
