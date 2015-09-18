import sys

def puts(s):
    print s
    sys.stdout.flush()

l, x, r = 10, 200, 10 ** 9
for i in xrange(100):

    puts("? %d" % x)
    reply = int(raw_input())
    if reply == 1:
        l = x
        r -= 1
    if reply == -1:
        r = x - 1
        l = max(0, l - 1)
    if reply == 0:
        puts("! %d" % (x + i))
        break

    x = (l + r) / 2
