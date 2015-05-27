def judge(c,u,v):
    connect = set(G[c][u])
    visited = set([])
    while 1:
        for i in connect-visited:
            connect |= set(G[c][i])
            visited.add(i)
        if connect == visited: break
    return True if u in connect and v in connect else False

n,m = map(int,raw_input().split())
G = [[[] for _ in range(n)] for __ in range(m)]
for loop in range(m):
    a,b,c = map(int,raw_input().split())
    a -= 1; b -= 1; c -= 1
    G[c][b].append(a)
    G[c][a].append(b)
q = int(raw_input())
for loop in range(q):
    u,v = map(int,raw_input().split())
    u -= 1; v -= 1
    ans = 0
    for i in range(m):
        if judge(i,u,v):
            ans += 1
    print ans
