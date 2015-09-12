N = int(raw_input())
if N == 1:
    print "Not Prime"
    exit()

i = 2
while i * i <= N:
    if N % i == 0:
        N = str(N)
        if int(N[-1]) in [1,3,7,9] and sum(map(int,list(N))) % 3 != 0:
            print "Prime"
        else:
            print "Not Prime"
        break
    i += 1
else:
    print "Prime"
