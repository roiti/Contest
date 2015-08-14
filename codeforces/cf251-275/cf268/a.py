n = int(raw_input())
if n == 4 or n >= 8:
    print "YES"
    for i in range(1,(n-4)/4+1):
        print 4*i+2,"-",4*i+1,"=",1
        print 4*i+4,"-",4*i+3,"=",1
        print "1 - 1 = 0"
    if n%4 == 1:
        print n,"* 0 = 0"
    if n%4 == 2:
        print n,"* 0 = 0"
        print n-1,"* 0 = 0"
    if n%4 == 3:
        print n,"* 0 = 0"
        print n-1,"* 0 = 0"
        print n-2,"* 0 = 0"
    for i in range(1,(n-4)/4+1):
        print "1 + 0 = 1"
    print "1 * 2 = 2"
    print "2 * 3 = 6"
    print "4 * 6 = 24"
elif n == 5:
    print "YES"
    print "5 * 3 = 15"
    print "4 * 2 = 8"
    print "8 + 1 = 9"
    print "15 + 9 = 24"
elif n == 6:
    print "YES"
    print "6 * 5 = 30"
    print "4 * 2 = 8"
    print "3 - 1 = 2"
    print "30 - 8 = 22"
    print "22 + 2 = 24"
elif n == 7:
    print "YES"
    print "7 + 6 = 13"
    print "13 + 5 = 18"
    print "18 + 4 = 22"
    print "22 + 3 = 25"
    print "25 + 1 = 26"
    print "26 - 2 = 24"
else:
    print "NO"
