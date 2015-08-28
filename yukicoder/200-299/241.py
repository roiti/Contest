N = int(raw_input())
A = [int(raw_input()) for i in xrange(N)]

hist = [0] * 50
for a in A:
	hist[a] += 1

if N in hist[:N]:
	print -1
	exit()

priority = sorted([[h, i] for i, h in enumerate(hist[:N])], reverse = True)
used = [False] * N
ans = [-1] * N
for h, i in priority:
	for j in xrange(N):
		if A[j] != i and not used[j]:
			ans[j] = i
			used[j] = True
			break
	else:
		for j in xrange(N):
			if not used[j]:
				ans[j] = i
				used[j] = True
				break

if -1 not in ans:
	for a in ans:
		print a
else:
	print -1
