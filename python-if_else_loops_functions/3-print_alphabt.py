#!/usr/bin/python3
for l in range(97, 123 + 1):
    if chr(l) != 'e' and chr(l) != 'q':
        print("{}".format(chr(l)), end='')
