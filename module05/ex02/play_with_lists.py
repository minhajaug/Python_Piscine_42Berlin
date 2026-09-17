#!/usr/bin/env python3

l = [2, 8, 9, 48, 8, 22, -12, 2]
n = list(map(lambda y: y + 2, list(filter(lambda x: x > 5, l))))

print(l)
print(n)
