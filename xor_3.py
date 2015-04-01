#!/usr/bin/python

'''XOR 3 is a combo of 1 and 2, because it uses the message itself
and a key to XOR together.'''

import random
import string
from itertools import cycle

secret = raw_input("Enter your plaintext -> ")

def genKey(size = 16):
    key = ''.join(random.choice(string.ascii_uppercase) for i in range(size))
    return str(key)

def msgxor(message, key):
    output = ""
    for char, key_char in zip(message, cycle(key)):
        char1 = ord(char)
        char2 = ord(char)
        key_char = ord(key_char)
        char2 >>= 1
        output += chr((char1 ^ char2) ^ key_char)
    return output.encode("hex") + "$" + key.encode("hex") + "$"

def main():
    print msgxor(secret, genKey(random.randint(1,16)))

if __name__ == "__main__": main()
