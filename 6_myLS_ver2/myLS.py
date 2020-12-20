import os
import sys

def printStarsFunction():
    for i in range(80):
        print("*", end ='')

    print();
def openDirectoryFunction(path):
    return os.listdir(path)

printStarsFunction();
print("STARTING ls SIMULATOR. (print files inside given folder)")
printStarsFunction();

# Getting value from args or using dot

directoryFilesToBePrintedOut = None
if len(sys.argv) >= 2:
    if sys.argv[1] != None:
        directoryFilesToBePrintedOut = sys.argv[1]
    else:
        directoryFilesToBePrintedOut = '.'

#Opening directory
filesListInsideDir = openDirectoryFunction(directoryFilesToBePrintedOut);
for item in filesListInsideDir:
        print("Item: {0:30s}       ".format(item))