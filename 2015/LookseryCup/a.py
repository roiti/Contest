def judge(x, y):
	a = sorted([A[y][x], A[y + 1][x], A[y][x + 1], A[y + 1][x + 1]])
	if a == ["a", "c", "e", "f"]: return True
	else: return False

N, M = map(int, raw_input().split())
A = [raw_input() for i in xrange(N)]
ans = 0
for y in xrange(N - 1):
	for x in xrange(M - 1):
		if judge(x, y):
			ans += 1
print ans
