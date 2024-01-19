# 1. Prints out everything that's in a directory.

import os

directory = str(input("What directory do you want to walk? "))

for root, dirs, files in os.walk(directory, topdown=False):
    for name in files:
      print(os.path.join(root, name))
    for name in dirs:
      print(os.path.join(root, name))


