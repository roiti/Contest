x, a, b = map(int, raw_input().split()) 
print "A" if abs(a - x) < abs(b - x) else "B"
