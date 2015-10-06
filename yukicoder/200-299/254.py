alpha = "abcdefghijklmnopqrstuvwxyz"
N = int(raw_input())
S = ""

c = 0
while N:
    i = 1
    while i * (i + 1) / 2 + i * (i - 1) / 2 <= N: i += 1
    i -= 1
    S += (alpha[c] + alpha[(c + 1) % 26]) * (i - 1) + alpha[c]
    N -= i * (i + 1) / 2 + i * (i - 1) / 2
    c = (c + 2) % 26
print S
