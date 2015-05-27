N,K = map(int,raw_input().split())
S = raw_input()

cost = 0
prize = 0
for i in range(min(N,K)):
    if prize == 0: cost += 1
    else: prize -= 1
    prize += int(S[i])
if K <= N: print cost
else:
    ans = cost
    s = sum(map(int,list(S)))
    if s < N:
        ans += (N-s)*((K-N)/N)
        for i in range(K%N):
            if prize == 0: ans += 1
            else: prize -= 1
            prize += int(S[i])
    print ans