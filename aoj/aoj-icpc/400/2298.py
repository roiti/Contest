N,K,T,U,V,L = map(int,raw_input().split())
R = [0]*L
D = [int(raw_input()) for i in range(N)]
dash = have = dashL = 0
for i in range(L):
	if i == dashL:
		if have == 0:
			dash = 0
		else:
			dashL = i + V*T
			have -= 1
	if i in D:
		if dash and have < K:
			have += 1
		else:
			dashL = i + V*T
			dash = 1
	if dash:
		R[i] = 1
print R.count(0)*1.0/U + R.count(1)*1.0/V

