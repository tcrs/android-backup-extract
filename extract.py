#!/usr/bin/python3

import collections
import struct
import zlib
import sys

def read_header(inp):
    buf = inp.read(24)

    lines = buf.decode('ascii').split('\n')
    if lines[0] != 'ANDROID BACKUP':
        raise ValueError('Header invalid')
    if lines[1] != '4':
        raise ValueError('Unsupported version')
    if lines[2] != '1':
        raise ValueError('Uncompressed not supported')
    if lines[3] != 'none':
        raise ValueError('Encryption not supported!')

def flate_stream(inp):
    d = zlib.decompressobj()
    buf = inp.read(4096)
    while buf:
        yield d.decompress(buf)
        buf = inp.read(4096)
    yield d.flush()

if __name__ == '__main__':
    hdr = read_header(sys.stdin.buffer)
    for buf in flate_stream(sys.stdin.buffer):
        sys.stdout.buffer.write(buf)

