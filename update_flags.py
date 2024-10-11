"""UPdate CFLAGS of Makefile

make -f Makefile_noGL -j 10
make clean -f Makefile_noGL
"""
import os
import fnmatch

def find_files(name, path):
  """Finds all files with the given name in the given path."""
  result = []
  for root, dirs, files in os.walk(path):
    for file in files:
      if fnmatch.fnmatch(file, name):
        result.append(os.path.join(root, file))
  return result

# Example usage
files = find_files("Makefile", "./Samples/")
verbose = False
if verbose:
    print(files) 
    print(len(files))

import fileinput

for file in files:
    if verbose:
        print(file)
    for line in fileinput.input(file, inplace=True):
        line = line.rstrip()
        if "ALL_CCFLAGS :=" in line:
            line = "ALL_CCFLAGS := -lineinfo" 
            print(line)
        else:
            print(line)
