#!/usr/bin/env python3 

import re, sys

if (len(sys.argv) != 3 or len(re.findall(sys.argv[1], sys.argv[2])) == 0):
     print("none")
else:
    k = sys.argv[1]
    s = sys.argv[2]
    print(len(re.findall(k, s)))

