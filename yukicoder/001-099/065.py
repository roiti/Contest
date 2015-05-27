def E(x,K):
    if x >= K: return 0.0
    else:
        if memo[x]: return memo[x]
        p = 1.0/6.0
        memo[x] = sum(E(x+i,K)*p for i in range(1,7))+1
        return memo[x]

K = int(raw_input())
memo = [0]*21
print E(0,K)