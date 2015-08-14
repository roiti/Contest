N, D, K = map(int, raw_input().split())
lr = [map(int, raw_input().split()) for i in xrange(D)]
st = [map(int, raw_input().split()) for i in xrange(K)]
 
ans = [0] * K
for i in xrange(D):
    l, r = lr[i]
    for j in xrange(K):
        s, t = st[j]
        if s == t: continue
        
        if l <= min(s, t) <= max(s, t) <= r:
            ans[j] = i + 1
            st[j][0] = t
        elif l <= s <= r:
            if t < l:
                st[j][0] = l
            elif r < t:
                st[j][0] = r
 
for i in ans:
    print i
