ref="ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
while 1:
	n=input()
	if n==0:break
	key=map(int,raw_input().split())
	code=list(raw_input())
	for i in range(len(code)):
		code[i]=ref[(ref.index(code[i])+key[i%n])%52]
	print "".join(map(str,code))

