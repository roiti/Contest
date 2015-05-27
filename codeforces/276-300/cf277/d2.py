mod = 1000000007

def dfs(u,f,root):
    res = 1
    for v in G[u]:
        if (v == f) or (a[v] > a[root]) or (a[v] == a[root] and v > root) or (a[root]-a[v] > d) :
            continue
        res = res*(dfs(v,u,root)+1)%mod
    return res

G = [[] for _ in range(2001)]
d,n = map(int,raw_input().split())
a = map(int,raw_input().split())

for i in range(n-1):
    u,v = map(int,raw_input().split())
    u-=1; v-=1
    G[u].append(v)
    G[v].append(u)

res=0
for i in range(n):
    ans = dfs(i,-1,i)
    res = (res+ans)%mod

print res
