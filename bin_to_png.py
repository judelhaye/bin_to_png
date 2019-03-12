#!/usr/bin/python
# coding: utf-8

import sys
import math
import os.path

from PIL import Image, ImageDraw

binary=sys.argv[1]
bin_name=binary.split("/")[-1]
print("converting {} ...".format(binary))
bitlist=[]
with open(binary, "rb") as f:
    
    byte = f.read(1)
    while byte != b'':
        bitlist.append(ord(byte))
        byte = f.read(1)

dimension = math.floor(math.sqrt((len(bitlist)/2)))
img = Image.new('RGB', (dimension,dimension))
count = 0
for row in range(dimension):
    for col in range(dimension):
        (r,g,b) = ((bitlist[count] & 0b00110000) << 2, (bitlist[count] & 0b00001100) << 4, (bitlist[count] & 0b00000011) << 6)
        img.putpixel((col,row), (r, g, b))
        count += 1

img.save("{}.png".format(bin_name))
