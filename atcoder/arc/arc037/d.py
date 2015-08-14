mod = 10**9 + 7
 
L = int(raw_input())
a, b, c = [0]*100010, [0]*100010, [0]*100010
a[0] = b[0] = c[0] = 1
for i in xrange(L):
    a[i + 1] = (3 * a[i] + pow(b[i] + c[i], 3, mod)) % mod
    b[i + 1] = (2 * b[i] * b[i] % mod * c[i] + b[i] * c[i] % mod * c[i]) % mod
    c[i + 1] = ((b[i] + c[i]) ** 2 + 2 * b[i] * c[i] % mod * c[i] + c[i] * c[i] % mod * c[i]) % mod
print a[L] % mod
