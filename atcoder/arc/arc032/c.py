import sys
sys.setrecursionlimit(100000)
 
def dfs(i):
    visited[i] = True
    for j in G[i]:
        if not visited[j]:
            dfs(j)
            
N,M = map(int,raw_input().split())
G = [[] for _ in range(N)]
for loop in range(M):
    a,b = map(int,raw_input().split())
    a,b = a-1,b-1
    G[a].append(b), G[b].append(a)
    
visited = [False]*N
cnt = 0
for i in range(N):
    if visited[i]: continue
    dfs(i)
    cnt += 1
    
print cnt-1
