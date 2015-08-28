A = map(int, raw_input().split())
three = two = 0
for a in set(A):
	if A.count(a) == 3:
		three += 1
	if A.count(a) == 2:
		two += 1

if   three and two: print "FULL HOUSE"
elif three: print "THREE CARD"
elif two == 2: print "TWO PAIR"
elif two == 1: print "ONE PAIR"
else: print "NO HAND"
