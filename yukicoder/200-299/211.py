K = int(raw_input())
p = [2,3,5,7,11,13]
n = [4,6,8,9,10,12]
ans = 0.0
for i in p:
    for j in n:
        if i * j == K: ans += 1 / 36.0
print ans