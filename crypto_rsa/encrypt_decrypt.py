#!/usr/bin/python3

import sys
from Crypto.PublicKey import RSA

def checkreq():
    if len(sys.argv) != 5:
        print("Usage:", sys.argv[0], "[e | d]", "[file]", "[key]", "[output]")
        sys.exit(1)

def main():
    checkreq()
    
    mode = sys.argv[1]
    file_location = sys.argv[2]
    output_location = sys.argv[4]
    key = RSA.importKey(open(sys.argv[3], 'r').read())

    with open(file_location, 'rb') as f:
        file_bytes = f.read()

    if mode == "e":
        obtained = key.encrypt(file_bytes, '')[0]
    elif mode == "d":
        obtained = key.decrypt(file_bytes)
    else:
        print("Available modes: 'e' for encrypt and 'd' for decrypt")
        sys.exit(1)

    with open(output_location, 'wb') as f:
        f.write(obtained)

if __name__ == "__main__":
    main()
