#!/bin/bash

# Ask user where the image is.
# Need to have analyzeMFT installed.
# pip install analyzeMFT
#
echo where is your image? 

read image

# Runs mmls first for $mft offset number.
mmls $image

# Run icat to create the mft image.
icat -o $offset $image 0 > mft.raw

echo what is the mft offset not including preceding 0s.

read offset

# Parse with analyzeMFT.
analyzeMFT.py -f mft.raw -o mftanalyzed.csv
