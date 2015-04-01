#!/usr/bin/python

'''Inspired by my man Ceasar.'''

from string import maketrans

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

secret = raw_input("Enter your plaintext -> ")
key = raw_input("Enter your key (1-25, 27-51) -> ")
key = int(key)

def cypher_make(key):
    replace = alphabet[key:] + alphabet[:key]
    return str(replace)

def string_cypher(message, translated):
    trans = maketrans(alphabet, translated)
    return message.translate(trans)

def main():
    print string_cypher(secret, cypher_make(key))

if __name__ == "__main__": main()
