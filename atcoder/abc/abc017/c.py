MAX = 10**5+10
a = [0]*MAX
n,m = map(int,raw_input().split())
 
su = 0
for loop in range(n):
    l,r,s = map(int,raw_input().split())
    l -= 1; r -= 1
    a[l] += s
    a[r+1] -= s
    su += s
 
    
for i in range(1,m):
    a[i] += a[i-1]
 
print su-min(a[:m])
