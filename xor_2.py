#!/usr/bin/python

'''I attempted to make a XOR that didn't need a key.
The closest I got was using the same character shifted.'''

import random

secret = raw_input("Enter your plaintext -> ")

def msgxor(message):
    output = ""
    for char in message:
        char1 = ord(char)
        char2 = ord(char)
        char2 >>= 1
        output += chr(char1 ^ char2)
    return output.encode("hex")

def main():
    print msgxor(secret)

if __name__ == "__main__": main()
