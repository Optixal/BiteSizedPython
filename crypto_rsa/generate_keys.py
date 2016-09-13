#!/usr/bin/python3

import sys
from Crypto.PublicKey import RSA

def checkreq():
    if len(sys.argv) != 4:
        print("Usage:", sys.argv[0], "[bits]", "[public key out]", "[private key out]")
        sys.exit(1)

def main():
    checkreq()
    
    bits = int(sys.argv[1])
    key = RSA.generate(bits)

    with open(sys.argv[2], 'wb') as f:
        f.write(key.publickey().exportKey() + b'\n')

    with open(sys.argv[3], 'wb') as f:
        f.write(key.exportKey() + b'\n')

if __name__ == "__main__":
    main()
