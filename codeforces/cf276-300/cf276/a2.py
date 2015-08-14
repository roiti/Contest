a,m = map(int,raw_input().split())
for loop in range(1000000):
    a += a%m
    if a%m == 0:
        print "Yes"
        break
else:
    print "No"
