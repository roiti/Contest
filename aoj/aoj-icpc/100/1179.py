for _ in range(input()):
	y,m,d = map(int,raw_input().split())
	print 196470 - ((y-1)*195 + (y-1)/3*5 + 20*(m-1) - min(1,y%3)*((m-1)/2) + d-1)

