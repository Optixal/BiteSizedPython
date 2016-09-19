#!/usr/bin/python3

# Optixal

# All Print Representation is in Hex

# Encrypt ASCII plaintext
# Using AES-CBC PKCS#7
# with random 256-bit key
# and random 128-bit (16-byte) IV

import sys, codecs
from Crypto.Cipher import AES
from Crypto import Random

template = "{0:20}: {1:}"

def checkreq():
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "[plaintext]")
        sys.exit(1)

def hexify(s):
    return codecs.encode(s, 'hex').decode("UTF-8").upper()

def main():
    checkreq()
    print(template.format("Plaintext", sys.argv[1]))
    
    # Generate Random 256-bit Key and 128-bit IV
    key = Random.new().read(32)
    iv = Random.new().read(16)
    print(template.format("256-bit Key", hexify(key)))
    print(template.format("128-bit IV", hexify(iv)))

    # Convert and Pad Plaintext
    plaintext = sys.argv[1].encode()
    pad_len = 16 - (len(plaintext) % 16)
    plaintext += bytes([pad_len]) * pad_len

    # Encrypt
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    print(template.format("Ciphertext", hexify(ciphertext)))
    print(template.format("IV + Ciphertext", hexify(iv + ciphertext)))

if __name__ == "__main__":
    main()
