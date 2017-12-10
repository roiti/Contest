X, A, B = map(int, raw_input().split())
print "delicious" if A >= B else "safe" if B - A <= X else "dangerous"
