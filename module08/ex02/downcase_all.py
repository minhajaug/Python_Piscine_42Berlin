#!/usr/bin/env python3

import sys

def downcase_it(s):
    return s.lower()

if len(sys.argv) < 2:
    print("none")
else:     
    for a in sys.argv[1:]:
        print(downcase_it(a))
