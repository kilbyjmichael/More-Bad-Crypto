#!/usr/bin/python

'''I wanted to mess with actual math.'''

import random
import string

secret = raw_input("Enter your plaintext -> ")

def genKey(size = 16):
    key = ''.join(random.choice(string.ascii_uppercase) for i in range(size))
    return str(key)

def msgxor(message, key):
    output = ""
    for char, key_char in zip(message, key):
        char1 = ord(char)
        key_char1 = ord(key_char)
        output += chr((char1 * 2) / key_char1)
    return output.encode("hex") + "$" + key.encode("hex")

def main():
    print msgxor(secret, genKey(len(secret)))

if __name__ == "__main__": main()
