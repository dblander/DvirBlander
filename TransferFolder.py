#!/usr/bin/python
import shutil
import os
import sys

# Gets the folders of two file locations and moves the first folder location to the second one.
# Requires the absolute path of the folder.
def main(fold1, fold2):
    files = os.listdir(fold1)
    for f in files:
        shutil.move(fold1 + f, fold2)

if __name__ == '__main__':
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    main(folder1, folder2)