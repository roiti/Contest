def judge(x, y):
    if A[y][x] == "#": return True
    if memo[y][x] is not None: return memo[y][x]
    
    win = False
    if x + 1 < W: win |= not judge(x + 1, y)
    if y + 1 < H: win |= not judge(x, y + 1)
    if x + 1 < W and y + 1 < H: win |= not judge(x + 1, y + 1)
    memo[y][x] = win
    return win
    
H, W = map(int, raw_input().split())
A = [raw_input() for i in xrange(H)]
memo = [[None] * W for i in xrange(H)]
print "First" if judge(0, 0) else "Second"
