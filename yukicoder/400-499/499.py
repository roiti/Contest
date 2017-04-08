# -*- coding: utf-8 -*-

def base10to(n, b):
    if n/b:
        return base10to(n/b, b) + str(n%b)
    return str(n%b)

print base10to(int(raw_input()), 7)
