k = int(raw_input())
t = raw_input()

tmp = ""
cnt = 0
for c in t:
	if c != "s":
		if cnt == 0:
			tmp += c
		elif c < "s":
			if k >= cnt:
				tmp += c
				k -= cnt
			else:
				tmp += "s" * (cnt - k) + c
				k = 0
		else:
			tmp += "s" * cnt + c
		cnt = 0
	else:
		cnt += 1
if cnt > 0:
	tmp += "s" * cnt

ans = ""
for c in tmp[::-1]:
	if c == "s":
		if k > 0:
			k -= 1
		else:
			ans += c
	else:
		ans += c
ans = ans[::-1]

print ans
