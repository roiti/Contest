n, m = map(int, raw_input().split())
edge = [[] for i in xrange(n)]
for i in xrange(m):
	a, b = map(int, raw_input().split())
	a -= 1
	b -= 1
	edge[a].append(b)
	edge[b].append(a)

circle = []
d2 = odd = even = 0
used = [False] * n
for i in xrange(n):
	if not used[i]:
		dfs(i)


