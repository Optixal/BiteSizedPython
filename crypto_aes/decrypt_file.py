#!/usr/bin/python3

# Optixal

# Decrypt ASCII plaintext
# Using AES-CBC PKCS#7
# with provided 256-bit key

import sys, codecs
from Crypto.Cipher import AES
from Crypto import Random

template = "{0:20}: {1:}"

def checkreq():
    if len(sys.argv) != 3:
        print("Usage:", sys.argv[0], "[ciphertext file]", "[key file (hex)]")
        sys.exit(1)

def unhexify(s):
    return codecs.decode(s, 'hex')

def main():
    checkreq()
    
    # Read and Convert Key
    keyhex = open(sys.argv[2], 'r').read().strip()
    key = unhexify(keyhex)

    # Read and Extract Ciphertext File
    iv_ciphertext = open(sys.argv[1], 'rb').read()
    ciphertext = iv_ciphertext[16:]
    iv = iv_ciphertext[:16]

    # Decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    # Write Plaintext Bytes to Output File
    with open('.'.join(sys.argv[1].split('.')[:-1]), 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":
    main()
