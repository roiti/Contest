import sys
N = 123
while True:
    s, n = raw_input().split()
    if n.startswith("0"):
        exit("error")
    if s == "?":
        if int(n) <= N and n <= str(N):
            print "Y"
        elif N < int(n) and str(N) < n:
            print "Y"
        else:
            print "N"
        sys.stdout.flush()
    else:
        print N, n
        exit()
