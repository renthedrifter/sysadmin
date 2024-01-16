# 1. Prints out everything that's in a directory.

# TO DO
# 1. User input so the directory doesn't have to be hard coded. Or if it has to be hard coded make sure the 
#    user mounts whatever image in the /mnt/something directory. 

import os

for root, dirs, files in os.walk("/home/supato/Downloads/Learning-Python-for-Forensics", topdown=False):
    for name in files:
      print(os.path.join(root, name))
    for name in dirs:
      print(os.path.join(root, name))


