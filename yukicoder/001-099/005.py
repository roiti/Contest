L = int(raw_input())
N = int(raw_input())
W = sorted(map(int,raw_input().split()))
ans = 0
X = 0
for w in W:
    if X+w > L: break
    X += w
    ans += 1
print ans