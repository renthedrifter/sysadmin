#!/bin/bash

# Ask user where the image is.
# Needs absolute path.
# Gets information about file system and disk.
#
echo where is your image? 

read image

fsstat $image
mmls $image
