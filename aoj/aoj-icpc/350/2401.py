import itertools as it
T,F = True,False

while 1:
    s = raw_input()
    if s == "#": break
    while "--" in s: s = s.replace("--","")
    for b,a in zip(["=","->","-","*","+"],[") == ("," != 1 or "," not "," and "," or "]):
        s = s.replace(b,a)
    s = "("+s+")"
    for v in xrange(2**11):
        a,b,c,d,e,f,g,h,i,j,k = map(int,list(format(v,"b").zfill(11)))
        if not eval(s):
            print "NO"
            break
    else:
        print "YES"


