def solve(Mi,i):
	if Mi == 0: return True
	if i < n and min(A[i:]) <= Mi <= sum(A[i:]):
		r1 = solve(Mi-A[i],i+1)
		if r1: return r1
		r2 = solve(Mi,i+1)
		if r2: return r2
n = input()
A = map(int,raw_input().split())
q = input()
M = map(int,raw_input().split())
for Mi in M:
	print "yes" if solve(Mi,0) else "no"

