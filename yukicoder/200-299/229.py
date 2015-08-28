def gcd(a, b):
	while b: a, b = b, a % b
	return a

def lcm(a, b):
	return a / gcd(a, b) * b

T1 = int(raw_input())
T2 = int(raw_input())
T3 = int(raw_input())

x = lcm(T1, T2)

print "%d/%d" % (lcm(lcm(T1, T2), T3), gcd(gcd(T1, T2), T3))
print T1 * T2 * T3 / lcm(lcm(T1, T2), T3)
