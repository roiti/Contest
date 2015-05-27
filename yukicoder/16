mod = 1000003
def pow_mod(x,y,mod):
    res = 1
    while y:
        if y & 1: res = (res * x) % mod
        x = x * x % mod
        y >>= 1
    return res
    
x,N = map(int,raw_input().split())
a = map(int,raw_input().split())
ans = 0
for ai in a:
    ans = (ans + pow_mod(x,ai,mod)) % mod
print ans