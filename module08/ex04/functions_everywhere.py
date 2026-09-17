#!/usr/bin/env python3
import sys

def shrink(s):
    return s[:8]
def enlarge(s):
    return (s + 'Z' * (8 - len(s)))

if len(sys.argv) <= 1:
    print ("none")
else:
    for a in sys.argv[1:]:
        if len(a) > 8: 
            print(shrink(a))
        elif len(a) < 8:
            print(enlarge(a))
        else:
            print(a)
    
