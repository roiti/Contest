n = int(raw_input())
tree = [[] for _ in range(n)]
deg,s = [],[]
for loop in range(n):
    a,b = map(int,raw_input().split())
    deg.append(a)
    s.append(b)

deg1 = [i for i in range(n) if deg[i] == 1]
cnt = 0
while deg1:
    ndeg1 = []
    for i in deg1:
        if deg[i] != 1: continue
        v = s[i]
        for l in tree[i]: v ^= l
        if v == i or v in tree[i]: continue
        tree[i].append(v)
        tree[v].append(i)
        deg[i] -= 1
        deg[v] -= 1
        if deg[v] == 1: ndeg1.append(v)
        cnt += 1
    deg1 = ndeg1[:]

print cnt
for i in range(n):
    for e in tree[i]:
        print i,e
        tree[e].remove(i)
