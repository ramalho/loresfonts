"""Convert font description from text to packed bytes"""

import sys
import struct

CHAR_PATTERN = '=c7B'

def read_pattern(infile):
    lin = infile.readline()
    code, char = lin[:-1].split(' ', 1)
    code = int(code)
    pattern = 0
    assert code == ord(char)
    pattern = []
    for i in range(7):
        lin = infile.readline()
        _, val = lin.rsplit(' ', 1)
        val = int(val)
        assert 0 <= val < 256
        pattern.append(val)
    return bytes([code]), pattern

file_name = sys.argv[1]
with open(file_name, 'rt') as infile, open(file_name + '.bin', 'wb') as outfile:
    while True:
        code, pattern = read_pattern(infile)
        print(code, pattern)
        outfile.write(struct.pack(CHAR_PATTERN, code, *pattern))
