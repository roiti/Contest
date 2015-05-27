echo a,b,c,d = map(int,raw_input().split())
misha = max(3.0*a/10.0,a-a/250.0*c)
vasya = max(3.0*b/10.0,b-b/250.0*d)
if misha > vasya:
    print "Misha"
elif misha < vasya:
    print "Vasya"
else:
    print "Tie"
