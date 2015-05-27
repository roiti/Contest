def factor(n):
    i = 2
    res = []
    while i*i <= n:
        tmp = 0
        while n%i == 0:
            tmp += 1
            n /= i
        if tmp > 0: res.append([i,tmp])
        i += 1
    if n > 1:
        res.append([n,1])
    return res

a,b = map(int,raw_input().split())
if a == b:
    print "infinity"
else:
    ans = 0
    fact = factor(a-b)
    ls = [1]
    for i,j in fact:
        ls += [ele*(i**k) for k in range(1,j+1) for ele in ls]
    print sum(1 for ele in ls if ele > b)
