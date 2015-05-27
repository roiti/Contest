X = int(raw_input())
Y = int(raw_input())
L = int(raw_input())
ans = (2 if Y < 0 else (1 if X != 0 else 0)) + (abs(X)+L-1)/L + (abs(Y)+L-1)/L
print ans