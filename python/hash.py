# 1. Hash all files in a directory.

# Problems.
# 1. None, yet.

import hashlib
import os

for root, dirs, files in os.walk("/home/supato/Downloads/Learning-Python-for-Forensics", topdown=False):
    for name in files:
      print(os.path.join(root, name))
    for name in dirs:
      print(os.path.join(root, name))

h = hashlib.md5(dirs)

