def buble(C):
	for i in range(len(C)):
		for j in range(len(C)-1,i,-1):
			if int(C[j][-1]) < int(C[j-1][-1]):
				C[j],C[j-1] = C[j-1],C[j]
	return C
	
def selection(C):
	for i in range(len(C)):
		mini = i
		for j in range(i,len(C)):
			if int(C[j][-1]) < int(C[mini][-1]):
				mini = j
		C[i],C[mini] = C[mini],C[i]
	return C

n = int(raw_input())
card = map(str, raw_input().split())
card1 = card[:]
buble(card);selection(card1)
print " ".join(map(str, card))
print "Stable"
print " ".join(map(str, card1))
print "Stable" if card == card1 else "Not stable"

