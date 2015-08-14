x, y = map(int, raw_input().split())
k = int(raw_input())
if y >= k:
	print x + k
else:
	print x - (k - y) + y
