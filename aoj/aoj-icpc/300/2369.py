cat = ["mew","mcecw","mcew","mecw"]
a = raw_input()
while any(i in a for i in cat):
	for i in cat: a = a.replace(i,"c")
print "Cat" if a == "c" else "Rabbit"

