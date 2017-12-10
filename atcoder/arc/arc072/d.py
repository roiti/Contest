# -*- coding: utf-8 -*-
X, Y = map(int, raw_input().split()) 
alice, brown = "Alice", "Brown"

hand = 0
while max(X, Y) >= 2:
    if X >= Y:
        i = X/2
        X -= 2*i
        Y += i
    else:
        i = Y/2
        Y -= 2*i
        X += i
    hand = (hand + 1)%2

print [brown, alice][hand]
