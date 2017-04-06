# -*- coding: utf-8 -*-
s = raw_input()
start = s.index("A")
end = s.rindex("Z")
print end - start + 1
