while 1:
	n,m,p=map(int,raw_input().split())
	if n==0:break
	x=[int(raw_input()) for i in range(n)]
	print (100-p)*sum(x)/x[m-1] if x[m-1]!=0 else 0

