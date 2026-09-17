#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3) or (int(sys.argv[1]) > int(sys.argv[2])):
    print("none")
else: 
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    l = []
    for i in range(x, y+1):
        l.append(i)

    print(l)
        

    

