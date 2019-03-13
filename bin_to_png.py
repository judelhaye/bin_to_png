#!/usr/bin/python
# coding: utf-8

import sys
import math
import os.path
import argparse

from PIL import Image, ImageDraw

def main(argv):
    parser = argparse.ArgumentParser(
            description='gives a visual representation of \
                            a binary file')
    parser.add_argument('input_file')
    parser.add_argument('output_file')

    args = parser.parse_args()
    input_file = args.input_file
    if not os.path.isfile(input_file):
        sys.exit('Error: {} is not a file'.format(input_file))

    print("transforming {} into png ...".format(input_file))
    bitlist=[]
    with open(input_file, "rb") as f:
        byte = f.read(1)
        while byte != b'':
            bitlist.append(ord(byte))
            byte = f.read(1)
    dimension = int(math.floor(math.sqrt((len(bitlist)/2))))

    img = Image.new('RGB', (dimension,dimension))
    count = 0
    for row in range(dimension):
        for col in range(dimension):
            (r,g,b) = ((bitlist[count] & 0b00110000) << 2,
                        (bitlist[count] & 0b00001100) << 4,
                        (bitlist[count] & 0b00000011) << 6)
            img.putpixel((col,row), (r, g, b))
            count += 1

    output_file = args.output_file
    img.save(output_file)

if __name__ == '__main__':
    main(sys.argv)
