#!/usr/bin/python

import random
import string

secret = raw_input("Enter your plaintext -> ")

def genKey(size = 16):
    key = ''.join(random.choice(string.ascii_uppercase) for i in range(size))
    return str(key)

def msgxor(message, key):
    output = ""
    for char, key_char in zip(message, key):
        output += chr(ord(char) ^ ord(key_char))
    return output.encode("hex") + "$" + key.encode("hex")

def main():
    print msgxor(secret, genKey(len(secret)*2))

if __name__ == "__main__": main()
