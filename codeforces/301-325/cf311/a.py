n = int(raw_input())
min1, max1 = map(int, raw_input().split())
min2, max2 = map(int, raw_input().split())
min3, max3 = map(int, raw_input().split())

maxs = [max1, max2, max3]
ans = [min1, min2, min3]
n -= min1 + min2 + min3

i = 0
while n and i < 3:
	if ans[i] < maxs[i]:
		ans[i] += 1
		n -= 1
	else:
		i += 1

print " ".join(map(str, ans))
