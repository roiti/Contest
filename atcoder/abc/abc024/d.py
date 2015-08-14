mod = 10 ** 9 + 7
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
 
C = (b * c - a * c) * pow(b * a - b * c + a * c, mod - 2, mod) % mod
R = (b * c - a * b) * pow(c * a - b * c + a * b, mod - 2, mod) % mod
print C, R
