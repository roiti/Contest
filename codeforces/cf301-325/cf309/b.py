n, k = map(int, raw_input().split())
m = 2 ** (n - 1)
p = 0
i = 0
ans = range(1, n + 1)

while k:
	if k >= m:
		ans[i:n - p - 1 - i] = ans[i:n - p - 1 - i][::-1]
		k -= m
		i = p
		p = 0
	else:
		m -= 2 ** p
		p += 1

print " ".join(map(str, ans))
