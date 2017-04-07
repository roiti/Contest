W = ["dream", "dreamer", "erase", "eraser"]
S = raw_input()

while S:
    for w in W:
	if S.endswith(w):
             S = S[:-len(w)]
             break
    else:
        print "NO"
        break
else:
    print "YES"
