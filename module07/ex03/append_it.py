#!/usr/bin/env python3

import sys

if len(sys.argv) <= 1:
    print("none")
else: 
    s = "ism"
    for a in sys.argv[1:]:
        if a.find(s) < 0:
           print(a + s)
            
