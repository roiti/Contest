from collections import defaultdict
n = int(raw_input())
l = map(int, raw_input().split())
d = map(int, raw_input().split())
ld = zip(l, d)
ld.sort(key = lambda x: x[1], reverse = True)

hist = defaultdict(int)
cost = defaultdict(int)
for li, di in zip(l, d):
	hist[li] += 1
	cost[li] += di

ans = 10 ** 9
cost_sum = sum(d)
for li, m in hist.items():
	c = cost_sum
	c -= cost[li]

	rem = m - 1
	for lj, dj in ld:
		if rem == 0: break
		if lj < li:
			rem -= 1
			c -= dj
	ans = min(ans, c)

print ans
