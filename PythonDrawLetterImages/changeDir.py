#!/usr/bin/python
import os

# Check current working directory.
currentPath = os.getcwd()
print("Current working directory %s" % currentPath)

# Move back one folder
# path = os.path.normpath(os.getcwd() + os.sep + os.pardir)

path = os.path.join(currentPath, "/Fonts/")

print("New working directory %s" % path)

os.chdir(path)