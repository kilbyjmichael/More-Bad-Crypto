#!/usr/bin/python

'''When using XOR, it is recomended to have a key as long as your message
to stop repeating characters. Repeating characters are discoverable, using
repeated space or character searching.'''

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
    print msgxor(secret, genKey(len(secret)))

if __name__ == "__main__": main()
