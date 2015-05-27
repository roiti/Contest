from collections import defaultdict
 
T = int(raw_input())
 
for loop in xrange(T):
    s = raw_input()
    n = len(s)
    
    hist = defaultdict(int)
    for c in s:
        hist[c] += 1
    hist = sorted([[v,c] for c, v in hist.items()], reverse = True)
    
    s = ""
    for v, c in hist:
        s += c * v
        
    s1 = s[:(n + 1) / 2]
    s2 = s[(n + 1) / 2:]
    ans = "".join(s1[i / 2] if i % 2 == 0 else s2[i / 2] for i in xrange(n))
    for i in xrange(1, n):
        if ans[i] == ans[i - 1]:
            print -1
            break
    else:
        print ans 
