a,b,c = map(int,raw_input().split())
x,y = a+b,a-b
if   x == y == c: print "?"
elif x == c: print "+"
elif y == c: print "-"
else: print "!"
