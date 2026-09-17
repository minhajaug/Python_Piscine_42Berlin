#!/usr/bin/env python3

import sys, re

if len(sys.argv) == 2 and len(re.findall("z", sys.argv[1])) != 0:
    for z in re.findall("z", sys.argv[1]):
        print(z, end="")
    print()
else:
    print("none")
