# Get attribute information from at file.

import os
import pathlib
import datetime

#p = pathlib.Path('/home/supato/programming/python/hash.py')
p = pathlib.Path(str(input("What file do you want to display attributes for? ")))
st = p.stat()

print("Access Time")
print(datetime.datetime.fromtimestamp(p.stat().st_atime))
print("Modified Time")
print(datetime.datetime.fromtimestamp(p.stat().st_mtime))
print("Create Time")
print(datetime.datetime.fromtimestamp(p.stat().st_ctime))

