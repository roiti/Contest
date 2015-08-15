import sys
 
H, W = map(int, raw_input().split())
A = [[-1] * W for i in xrange(H)]
if (H * W) % 2 == 1:
    print "First"
    sys.stdout.flush()
    print (H + 1) / 2, (W + 1)/ 2, 0
    sys.stdout.flush()
else:
    print "Second"
    sys.stdout.flush()
 
while 1:
    a, b, c = map(int, raw_input().split())
    if (a, b, c) == (-1, -1, -1): break
    print H + 1 - a, W + 1 - b, (c if (H * W) % 2 == 1 else 1 - c)
    sys.stdout.flush()
