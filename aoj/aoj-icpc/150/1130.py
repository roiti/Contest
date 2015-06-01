def solve(w,h):
	if 0 <= w < W and 0 <= h < H and tile[h][w] == ".":
		tile[h][w] = 0
		solve(w+1,h); solve(w,h+1); solve(w-1,h); solve(w,h-1)
while 1:
	W,H = map(int,raw_input().split())
	if W == 0: break
	tile = [list(raw_input()) for i in range(H)]
	for h in range(H):
		try:
			sw = tile[h].index("@")
			sh = h
			tile[sh][sw] = "."
			break
		except:
			pass
	solve(sw,sh)
	print sum(tile[h].count(0) for h in range(H))

