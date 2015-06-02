from __future__ import division, print_function
from sys import stdin

i = 1
for line in stdin:
    x = int(line)
    if not x:
       break
    print ('Case {}: {}'.format(i, x))
    i += 1

