N, A, B = map(int, raw_input().split())
while 1:
    N -= A
    if N <= 0:
        print "Ant"
        break
    N -= B
    if N <= 0:
        print "Bug"
        break

