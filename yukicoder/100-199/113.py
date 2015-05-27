S = raw_input()
x,y = abs(S.count("N")-S.count("S")),abs(S.count("E")-S.count("W"))
print (x*x+y*y)**0.5