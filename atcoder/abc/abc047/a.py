a, b, c = map(int, raw_input().split())
print "Yes" if a == b + c or b == c + a or c == a + b else "No"
