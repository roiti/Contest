import itertools
while 1:
    t,s = map(int,raw_input().split())
    if t == 0: break
    ans = s if s <= t else 0
    s = str(s)
    nums = [s] if ans > 0 else []
    n = len(s)
    reject = False
    for split in xrange(1,n):
        for cuts in itertools.combinations(range(1,n),split):
            cuts = [0]+list(cuts)+[n]
            tmp = sum(int(s[i:j]) for i,j in zip(cuts,cuts[1:]))
            if   tmp == ans: reject = True
            elif t >= tmp > ans:
                ans = tmp
                nums = [s[i:j] for i,j in zip(cuts,cuts[1:])]
                reject = False
    if reject: print "rejected"
    elif len(nums) == 0: print "error"
    else: print ans, " ".join(nums)

