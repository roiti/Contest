N, L = map(int, raw_input().split())

xd = [raw_input().split() for i in xrange(N)]
xd = [[int(x), d] for x, d in xd]

ans = 0
r, l = [], []
bx, cnt = 0, 0
for x, d in xd:
	if d == "R":
		ans += cnt * (x - bx - 1)
		cnt += 1
		bx = x
	elif cnt > 0:
		r.append([bx, cnt])
		cnt = 0
if cnt > 0:
	r.append([bx, cnt])

bx, cnt = L, 0
for x, d in reversed(xd):
	if d == "L":
		ans += cnt * (bx - x - 1)
		cnt += 1
		bx = x
	elif cnt > 0:
		l.append([bx, cnt])
		cnt = 0
if cnt > 0:
	l.append([bx, cnt])

l = l[::-1]

if len(l) > 0:
	if len(r) == 0 or l[0][0] < r[0][0]:
		ans += l[0][1] * (l[0][0] - 1)
		l.pop(0)

if len(r) > 0:
	if len(l) == 0 or l[-1][0] < r[-1][0]:
		ans += r[-1][1] * (L - r[-1][0])
		r.pop()

for i in xrange(len(r)):
	rx, rcnt = r[i]
	lx, lcnt = l[i]
	ans += max(rcnt, lcnt) * (abs(rx - lx) - 1)

print ans
