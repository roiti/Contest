N = int(raw_input())
if N == 1:
    print "Aoki"
    exit()
    
b = bin(N)[2:]
lb = len(b)
mx = mn = 1
for i in xrange(lb - 2):
    mx = 2 * mx + 1 if i % 2 == 0 else 2 * mx
for i in xrange(lb - 2):
    mn = 2 * mn if i % 2 == 0 else 2 * mn + 1
 
if lb % 2 == 0:
    if 2 * mn <= N:
        print "Takahashi"
    else: 
        print "Aoki"
else:
    if 2 * mx <= N:
        print "Aoki"
    else:
        print "Takahashi"
