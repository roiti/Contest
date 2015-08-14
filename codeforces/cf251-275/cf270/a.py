def isprime(n):
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True
            
n = int(raw_input())
for i in xrange(2,n):
    if isprime(i) or isprime(n-i): continue
    print i,n-i
    break
