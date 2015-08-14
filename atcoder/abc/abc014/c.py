L = 1000002
hist = [0]*L
n = int(raw_input())
for roop in range(n):
    a,b = map(int,raw_input().split())
    hist[a] += 1
    hist[b+1] -= 1
tmp = 0
for i in range(L):
    tmp += hist[i]
    hist[i] = tmp
print max(hist)
