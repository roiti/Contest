s = raw_input()
k = int(raw_input())
n = len(s)
if n % k != 0:
    print "NO"
else:
    d = n / k
    for i in xrange(0, n, d):
        if s[i:i + d] != s[i:i + d][::-1]:
            print "NO"
            break
    else:
        print "YES"
