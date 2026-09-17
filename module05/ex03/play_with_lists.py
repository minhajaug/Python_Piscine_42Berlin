#!/usr/bin/env python3
l = [2, 8, 9, 48, 8, 22, -12, 2]
s = set(l)
res = set(map(lambda x: x + 2, list(filter(lambda y: y > 5, s))))
print(l)
print(res)
