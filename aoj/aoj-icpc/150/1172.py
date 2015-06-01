r = 2*123456+1
s = int(r**0.5)
p = [1]*r
p[0] = p[1] = 0
for i in range(s):
	if p[i]:
		p[2*i::i] = [0 for x in range(2*i,r,i)]

while 1:
	n = input()
	if n == 0: break
	print sum(p[n+1:2*n+1])

