import os
import fnmatch

keywords = '/home/supato/Documents/testing/keys.txt'

for root, dirs, files in os.walk('/home/supato/Documents/testing'):
    for file in files:
        file = os.path.join(root, file)    
        with open(file) as f:
           for line in f:
              if 'secret' in line:
                 print (file, ": ", line.rstrip())
