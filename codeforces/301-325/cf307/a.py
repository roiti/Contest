n = int(raw_input())
a = map(int, raw_input().split())
b = sorted(a, reverse = True)

rank = [0] * 2001
for i in xrange(len(b)):
	if rank[b[i]] == 0:
		rank[b[i]] = i + 1

ans = [rank[ai] for ai in a]
print " ".join(map(str, ans))
