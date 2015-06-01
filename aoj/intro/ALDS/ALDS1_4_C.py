n = int(raw_input())
ls = {}
for i in range(n):
    inp = raw_input()
    if inp[0] == "i":
        ls[inp[7:]] = 1
    else:
        try:
        	if ls[inp[5:]] == 1: print "yes"
        except:
        	print "no"
            

