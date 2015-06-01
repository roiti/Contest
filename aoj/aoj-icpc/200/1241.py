R = 2**15+1
dp = [[0]*R for i in range(5)]
dp[0][0] = dp[1][0] = dp[2][0] = dp[3][0] = 1
for i in range(1,182):
	for k in range(1,5):
		for j in range(i*i,R):
			dp[k][j] += dp[k-1][j-i*i]

while 1:
	n = input()
	if n == 0: break
	print dp[4][n]

