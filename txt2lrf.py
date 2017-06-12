"""Convert font description from text to LRF format"""

import sys
import struct

LRF_MAGIC = b'LRF1'
HEADER_PATTERN = '>BBBH'
CHAR_PATTERN = '>c7B'

def read_pattern(infile):
    lin = infile.readline()
    if lin == '':
        raise EOFError
    assert lin.startswith('#')
    count, code, char = lin[1:-1].split(' ', 2)
    count = int(count)
    code = int(code)
    pattern = 0
    assert code == ord(char)
    pattern = []
    while True:
        lin = infile.readline()
        if lin.startswith('#') or len(lin) == 0:
            break
        _, val = lin.rsplit(' ', 1)
        val = int(val)
        assert 0 <= val < 256
        pattern.append(val)
    return bytes([code]), pattern

def convert(txt_path):
    base_path, ext = os.path.splitext(txt_path)
    glyph_records = []
    with open(txt_path, 'rt') as infile
        while True:
            try:
                code, pattern = read_pattern(infile)
            except EOFError:
                break
            print(code, pattern)
            glyph_records.append(struct.pack(CHAR_PATTERN, code, *pattern))
    lrf_path = base_path + '.lrf'
    with open(lrf_path, 'wb') as outfile:
        outfile.write(LRF_MAGIC)
        outfile.write(struct.pack(HEADER_PATTERN, ))

file_name = sys.argv[1]
