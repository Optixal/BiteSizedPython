#!/usr/bin/python3

import math, sys

if len(sys.argv) != 2:
    print("[*] Usage: python3", sys.argv[0], "[no. of bits]")
    sys.exit(1)

dec_length = math.floor(math.log10(2 ** int(sys.argv[1]))) + 1

print(str(dec_length))
