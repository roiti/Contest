p = [1]*10001
p[0] = p[1] = 0
for i in xrange(2,int(10001**0.5)):
    if p[i]: p[2*i::i] = [0]*len(p[2*i::i])
p = [i for i in xrange(10001) if p[i]]

N = int(raw_input())
dp = [0]*10001
dp[0] = dp[1] = 1
for i in xrange(1,10001):
    for j in p:
        if j > i: break
        if dp[i-j] == 0:
            dp[i] = 1
            break
print ["Lose","Win"][dp[N]]