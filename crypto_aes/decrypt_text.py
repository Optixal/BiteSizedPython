#!/usr/bin/python3

# Optixal

# All Print and Input Representation is in Hex

# Decrypt ASCII ciphertext
# Using AES-CBC PKCS#7
# with 256-bit key
# and 128-bit (16-byte) IV

import sys, codecs
from Crypto.Cipher import AES
from Crypto import Random

template = "{0:20}: {1:}"

def checkreq():
    if len(sys.argv) != 3:
        print("Usage:", sys.argv[0], "[iv + ciphertext hex]", "[key hex]")
        sys.exit(1)

def unhexify(s):
    return codecs.decode(s, 'hex')

def main():
    checkreq()
    
    ciphertext = unhexify(sys.argv[1])[16:]
    key = unhexify(sys.argv[2])
    iv = unhexify(sys.argv[1])[:16]
    print(template.format("IV + Ciphertext", sys.argv[1]))
    print(template.format("Ciphertext", sys.argv[1][32:]))
    print(template.format("256-bit Key", sys.argv[2]))
    print(template.format("128-bit IV", sys.argv[1][:32]))

    # Decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = plaintext[:-plaintext[-1]]
    print(template.format("Ciphertext", plaintext.decode("UTF-8")))

if __name__ == "__main__":
    main()
