alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
H, W = map(int, raw_input().split())
S = [raw_input().split() for i in xrange(H)]

for h in xrange(H):
	for w in xrange(W):
		if S[h][w] == "snuke":
			print alpha[w] + str(h + 1)
			exit()
