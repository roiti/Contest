A, B = map(abs, map(int, raw_input().split()))
print "Draw" if A==B else "Ant" if A < B else "Bug"
