while 1:
    n = int(raw_input())
    if n == 0: break
    exist = set([])
    enter = [0]*1000
    bless = [0]*1000
    for loop in xrange(n):
        md,hm,io,p = raw_input().split()
        h,m = map(int,hm.split(":"))
        t = 60*h+m
        p = int(p)
        if io == "I":
            enter[p] = t
            exist.add(p)
        else:
            exist.remove(p)
            if p == 0:
                for i in exist: bless[i] += t-max(enter[p],enter[i])
            elif 0 in exist:
                bless[p] += t-max(enter[0],enter[p])
    print max(bless)
    

