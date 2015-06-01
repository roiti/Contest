ref = {"1":".,!? ",
	   "2":"abc",
	   "3":"def",
	   "4":"ghi",
	   "5":"jkl",
	   "6":"mno",
	   "7":"pqrs",
	   "8":"tuv",
	   "9":"wxyz"}
for _ in range(input()):
	inputs = map(str,raw_input().split("0"))
	ans = ""
	for input in inputs:
		if len(input) > 0:
			k = input[0]
			ans += ref[k][(len(input)-1)%len(ref[k])]
	print ans

