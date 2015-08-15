N = int(raw_input())
a = map(int, raw_input().split())
if N % 2 == 0:
    if min(a) == 1:
        print "Iori"
    elif sum(a) % 2 == 1:
        print "Iori"
    else:
        if (sum(a) - min(a)) % 2 == 1:
            print "Iori"
        else:
            print "Yayoi"
else:
    if sum(a) % 2 == 1:
        print "Iori"
    else:
        print "Yayoi"
