#!/usr/bin/python3

import base64
import argparse
from termcolor import cprint

rprint = lambda x: cprint(x, 'red')
gprint = lambda x: cprint(x, 'white')


def parseArgs():
    parser = argparse.ArgumentParser(description="Tries many different \
                    encodings so you can figure out WTF is this string")
    parser.add_argument('datafile', type=str,
                        help="The file with the data to decode")

    return parser.parse_args()


def baseDecode(data):
    try:
        gprint("Base16: " + str(base64.b16decode(data, casefold=True)))
    except Exception as e:
        rprint("Cannot be Base16 : " + str(e))

    try:
        gprint("Base32: " + str(base64.b32decode(data, casefold=True)))
    except Exception as e:
        rprint("Cannot be Base32 : " + str(e))

    try:
        gprint("Base64: " + str(base64.b64decode(data)))
    except Exception as e:
        rprint("Cannot be Base64 : " + str(e))

    try:
        gprint("Base85: " + str(base64.b85decode(data)))
    except Exception as e:
        rprint("Cannot be Base85 : " + str(e))

    try:
        gprint("Ascii85: " + str(base64.a85decode(data)))
    except Exception as e:
        rprint("Cannot be Ascii85 : " + str(e))


def main():
    args = parseArgs()

    try:
        wtfstring = open(args.datafile, 'rb').read()
    except Exception:
        rprint("Cannot open " + args.datafile)
        return

    baseDecode(wtfstring)

if __name__ == "__main__":
    main()
