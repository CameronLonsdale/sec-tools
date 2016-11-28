#!/usr/bin/python3

import string
import argparse
import base64
import binascii
import sys

# Coming Later
# def rotn(message, n=13):
#    code_alphabet = string.ascii_lowercase[n:] + string.ascii_lowercase[0:n]
#    return message.lower().translate(string.maketrans(string.ascii_lowercase, code_alphabet))

def parseArgs():
    parser = argparse.ArgumentParser(description="Tries many different \
                    encodings so you can figure out WTF is this string")
    parser.add_argument('datafile', type=str,
                        help="The file with the data to decode")

    args = parser.parse_args()
    return args

# Is there a way to iterate over these functions instead?
# Might be nicer
def baseDecode(data):
    try:
        print("Base16: " + str(base64.b16decode(data, casefold=True)))
    except binascii.Error:
        print("Cannot be Base16")

    try:
        print("Base32: " + str(base64.b32decode(data, casefold=True)))
    except binascii.Error:
        print("Cannot be Base32")

    try:
        print("Base64: " + str(base64.b64decode(data)))
    except binascii.Error:
        print("Cannot be Base64")

    try:
        print("Base85: " + str(base64.b85decode(data)))
    except:
        print("Cannot be Base85")

    try:
        print("Ascii85: " + str(base64.a85decode(data)))
    except:
        print("Cannot be Ascii85")

if __name__ == "__main__":
    try:
        wtfstring = open(parseArgs().datafile, 'r').read()
    except:
        print("Cannot Open file")
        sys.exit()

    baseDecode(wtfstring)
