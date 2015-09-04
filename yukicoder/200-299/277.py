import sys
sys.setrecursionlimit(1000000)

def dfs(i, d):
    R[i] = d
    used[i] = True
    if len(tree[i]) > 0:
        mn = 1e9
        for j in tree[i]:
            if not used[j]:
                mn = min(mn, dfs(j, d + 1))
        L[i] = mn
    L[i] = 0 if mn == 1e9 else mn
    return L[i] + 1

def dfs2(i, d):
    used[i] = True
    if d < L[i]:
        L[i] = d
    else:
        d = L[i]
    for j in tree[i]:
        if not used[j]:
            dfs2(j, d + 1)

N = int(raw_input())
tree = [[] for i in xrange(N)]

for loop in xrange(N - 1):
    x, y = map(int, raw_input().split())
    x -= 1
    y -= 1
    tree[x].append(y)
    tree[y].append(x)

R, L = [0] * N, [1e9] * N
used = [False] * N
dfs(0, 0)
used = [False] * N
dfs2(0, L[0])

for i in xrange(N):
    print min(R[i], L[i])
