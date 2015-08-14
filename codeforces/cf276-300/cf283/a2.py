n = int(raw_input())
a = map(int,raw_input().split())
ans = 10**10
for i in range(1,n-1):
    aa = a[:i] + a[i+1:]
    ans = min(ans,max(aa[j+1]-aa[j] for j in range(len(aa)-1)))
print ans
