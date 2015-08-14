def dfs(i):
    if len(buka[i]) == 0: return 1
    mx, mn = 1, 999999
    for j in buka[i]:
        tmp = dfs(j)
        mx = max(tmp, mx)
        mn = min(tmp, mn)
    return mx + mn + 1
 
N = int(raw_input())
buka = [[] for i in xrange(N)]
for i in xrange(N - 1):
    B = int(raw_input()) - 1
    buka[B].append(i + 1)
print dfs(0)
