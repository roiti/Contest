H, W = map(int, raw_input().split())    
print "#"*(W + 2)
for i in xrange(H):
    print "#" + raw_input() + "#"
print "#"*(W + 2)
