L = int(raw_input())
B = [int(raw_input()) for i in xrange(L)]
b = 0
for bi in B: b ^= bi
if b != 0:
    print -1
else:
    print 0
    for i in xrange(L - 1):
        b = B[i] ^ b
        print b
    
    
