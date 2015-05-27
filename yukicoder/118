mod = 10**9+7
N = int(raw_input())
h = [0]*100
for i in map(int,raw_input().split()): h[i-1] += 1
ans = 0
for i in range(100):
    for j in range(i+1,100):
        for k in range(j+1,100):
            ans = (ans+h[i]*h[j]*h[k]%mod)%mod
print ans
