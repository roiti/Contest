N = int(raw_input())
i = 2
while i * i <= N:
    if N % i == 0:
        print "NO"
        break
    i += 1
else:
    print "YES"
