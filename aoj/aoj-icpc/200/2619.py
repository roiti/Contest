import sys
sys.setrecursionlimit(9999)
def dfs(i, z):
    print "." * z + name[i]
    for j in child[i]:
        dfs(j, z + 1)

n = int(raw_input())
name = []
child = [[] for i in xrange(n)]
for i in xrange(n):
    k = int(raw_input())
    m = raw_input()
    name.append(m)
    if k == 0: continue
    child[k - 1].append(i)

dfs(0, 0)
