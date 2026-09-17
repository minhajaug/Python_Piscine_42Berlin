#!usr/bin/env python3

import sys

if len(sys.argv < 2):
    print("none")
else: 
    print(f"parameters: {len(sys.argv)}")
    for a in sys.argv:
        print(f"{a}: {len(a)}")
