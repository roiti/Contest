from collections import defaultdict
def makeb():
	return min(hista[k] / v for k, v in histb.items())

def makec():
	return min(hista[k] / v for k, v in histc.items())

alpha = "abcdefghijklmnopqrstuvwxyz"
a = raw_input()
b = raw_input()
c = raw_input()

_hista = defaultdict(int)
histb = defaultdict(int)
histc = defaultdict(int)
for ai in a: _hista[ai] += 1
for bi in b: histb[bi] += 1
for ci in c: histc[ci] += 1

ans1 = ans2 = ""
cnt1 = cnt2 = 0

hista = _hista.copy()
m, n = makeb(), makec()
ans1 += b * m
cnt1 += m
for k, v in histb.items():
	hista[k] -= m * v

n = makec()
cnt1 += n
ans1 += c * n
for k, v in histc.items():
	hista[k] -= n * v
for k, v in hista.items():
	ans1 += k * v

hista = _hista.copy()
m, n = makeb(), makec()
ans2 += c * n
cnt2 += n
for k, v in histc.items():
	hista[k] -= n * v
m = makeb()
cnt2 += m
ans2 += b * m
for k, v in histb.items():
	hista[k] -= m * v
for k, v in hista.items():
	ans2 += k * v

print ans1 if cnt1 > cnt2 else ans2
