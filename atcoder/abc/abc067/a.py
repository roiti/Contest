A, B = map(int, raw_input().split())
print "Possible" if min(A%3, B%3, (A + B)%3) == 0 else "Impossible"
