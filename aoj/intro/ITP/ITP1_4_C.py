while True:
    a, op, b = raw_input().split()
    a = int(a)
    b = int(b)
    if op == "?":
        break
    elif op == "+":
        print a + b
    elif op == "-":
        print a - b
    elif op == "*":
        print a * b
    elif op == "/":
        print a / b

