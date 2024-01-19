#!/bin/bash

# Ask user where the image is.
# Lists files and directories in a file system also displays information about deleted files. 
# 
#
echo where is your image? 

read image

fls -r -l $image | less

