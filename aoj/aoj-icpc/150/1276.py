r = 1299710
p = [1]*r
p[0] = p[1] = 0
for i in range(int(r**0.5)):
	if p[i]:
		p[2*i::i] = [0 for x in range(2*i,r,i)]

while 1:
	n = input()
	if n == 0: break
	l = r = n
	while p[l] == 0: l -= 1
	while p[r] == 0: r += 1
	print r - l

