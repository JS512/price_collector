import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.

grandparent_dir = os.path.abspath(os.path.join(current, ".."))

parent = os.path.dirname(grandparent_dir)
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
print(parent)