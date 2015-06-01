while 1:
	t,p,r=map(int,raw_input().split())
	if t==0:break
	wrong=[[0]*p for i in range(t)]
	point={i+1:[0,0] for i in range(t)}
	for i in range(r):
		tid,pid,time,msg=map(str,raw_input().split())
		tid,pid,time=int(tid),int(pid),int(time)
		if msg[0]=="W":
			wrong[tid-1][pid-1]+=1
		else:
			point[tid][0]+=1
			point[tid][1]+=1200*wrong[tid-1][pid-1]+time

	for k,v in sorted(sorted(point.items(),key=lambda x:x[1][1]),key=lambda x:x[1][0],reverse=True):
		print k,v[0],v[1]
	

