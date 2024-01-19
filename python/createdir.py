import os

dirname = str(input("What do you want to call the directory? "))

sub1 = "workspace"
sub2 = "evidence"
os.makedirs(os.path.join(dirname, sub1))
os.makedirs(os.path.join(dirname, sub2))
