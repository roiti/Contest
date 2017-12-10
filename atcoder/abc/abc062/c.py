H, W = map(int, raw_input().split())
ans = H*W 

for loop in xrange(2):
    ans = min(ans, (((H - H/3) + 1)/2 - H/3)*W)
    for w in xrange(1, W):
        h = H/2
        mx = max(w*H, (W - w)*(H - h))
        mn = min(w*H, (W - w)*h)
        ans = min(ans, mx - mn)
    H, W = W, H

print ans
