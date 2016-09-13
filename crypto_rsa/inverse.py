#!/usr/bin/python3

# inverse.py by optixal
# Constructs private exponent (d) from 2 prime factors (p, q) and public exponent (e)
# Usage: python3 inverse.py [p] [q] [e=65537]

import sys

def checkreq():
    if len(sys.argv) < 3:
        print("[*] Usage:", sys.argv[0], "[p]", "[q]", "[e=65537]")
        sys.exit(1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Mod inverse not found!")
    else:
        return x % m

def main():
    checkreq()

    p = int(sys.argv[1])
    q = int(sys.argv[2])
    print("Prime Factor p:", p)
    print("Prime Factor q:", q)
    
    n = p * q
    print("Modulus n:", n)
    
    totient = (p - 1) * (q - 1)
    print("Totient:", totient)

    # Usually e = 3 or 65537
    if len(sys.argv) == 4:
        e = int(sys.argv[3])
    else:
        e = 65537
    print("Public Exponent e:", e)

    d = modinv(e, totient)
    print("Private Exponent d:", d)

if __name__ == "__main__":
    main()
