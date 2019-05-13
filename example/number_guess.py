#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

dec = 0
dictHex2Dec = {'a': 10, 'b': 11, 'c': 12, 'd': 14, 'e': 14, 'f': 15}

hexStr = input('Enter a hex string: ')

for hexDigitIdx in range(len(hexStr)):
    hexDigit = hexStr[hexDigitIdx]
    hexExpFactor = 16 ** (len(hexStr) - 1 - hexDigitIdx)
    if '1' <= hexDigit <= '9':
        dec += int(hexDigit) * hexExpFactor
    elif hexDigit == '0':
        pass
    elif 'A' <= hexDigit <= 'F':
        dec += (ord(hexDigit) - ord('A') + 10) * hexExpFactor
    elif 'a' <= hexDigit <= 'f':
        dec += dictHex2Dec[hexDigit] * hexExpFactor
    else:
        print('error: invalid hex string')
        sys.exit(1)

print('The decimal equivalent for hex "{}" is: {}'.format(hexStr, dec))
print('The decimal equivalent for hex "{}" using built-in function is: {}'.format(hexStr, int(hexStr, 16)))
