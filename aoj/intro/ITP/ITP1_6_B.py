Sp = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Hu = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Cr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Dy = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num = int(input())
i = 0

while i < num:
     suit, n = raw_input().split()
     n = int(n)
     if suit == "S":
        Sp[n-1] = 0
     elif suit == "H":
        Hu[n-1] = 0
     elif suit == "C":
        Cr[n-1] = 0
     else:
        Dy[n-1] = 0
     i += 1

for i in Sp:
    if i != 0:
        print "S", i

for i in Hu:
    if i != 0:
        print "H", i

for i in Cr:
    if i != 0:
        print "C", i

for i in Dy:
    if i != 0:
        print "D", i


