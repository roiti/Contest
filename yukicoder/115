N,D,K=map(int,raw_input().split())
s=range(1,K)+[D-K*(K-1)/2]
for i in range(2,K+1):
    while s[-i]<=N-i and s[-1]>N:s[-i]+=1;s[-1]-=1
print " ".join(map(str,s)) if s[-2]<s[-1]<=N else -1