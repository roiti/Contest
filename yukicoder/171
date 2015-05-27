def fact(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res
    
S = raw_input()
hist = [0]*26
for s in S:
    hist[ord(s)-ord("A")] += 1
ans = fact(len(S))
for i in hist:
    ans /= fact(i)
print (ans-1)%573
