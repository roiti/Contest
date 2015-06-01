def isPrime(p):
	if p == 2: return 1
	if p < 2 or p&1 == 0: return 0
	return 1 if pow(2,p-1,p) == 1 else 0
	
n = int(raw_input())
print sum(isPrime(int(raw_input())) for i in range(n))

