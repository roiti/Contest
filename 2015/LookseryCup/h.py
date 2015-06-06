import math
a, b = map(int, raw_input().split())
c, d = map(int, raw_input().split())

ans = max(map(abs, [a, b, c, d]))
det = a * d - b * c
if det == 0:
	ans = 0
for x in [1, -1]:
	for y in [1, -1]:
		for z in [1, -1]:
			for w in [1, -1]:
				k = a * x + b * y + c * z + d * w
				if k != 0:
					ans = min(ans, abs(float(det) / k))
print "%.10f" % ans
