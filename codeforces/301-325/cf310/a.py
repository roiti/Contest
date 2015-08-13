n, k = map(int, raw_input().split())
ans = 0
part = k
for loop in xrange(k):
	a = map(int, raw_input().split())[1:]
	if a[0] == 1:
		for i in xrange(len(a) - 1):
			if a[i] + 1 < a[i + 1]:
				part += len(a) - i - 1
				ans += len(a) - i - 1
				break
	else:
		part += len(a) - 1
		ans += len(a) - 1

ans += part - 1
print ans
