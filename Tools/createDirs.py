# createDirs.py
# Create a directory tree from an unordered tab-indented directory list (TOC)

import os
import sys

dirsTreeRoot = '../Training/'   # relative to 'Tools/' directory
tocPath = '../'                 # relative to 'Tools/' directory
tocFile = 'Curriculum.md'       # should be save as UTF-8 without BOM (i.e., Byte Order Mark)
dirOrderFile = '.dirorder'

def createDirectories(tocFileObject):
    """"""
    parentsList = [dirsTreeRoot]
    parentLevel = -1
    try:
            for line in tocFileObject:
                folderName, level = getFolderNameAndIndentLevel(line)
                if folderName is None:
                    continue                # skip invalid lines
                if level <= parentLevel:    # going backward or staying in the current tree level
                    for i in range(parentLevel - level + 1):
                        parentsList.pop()
                folderPath = os.path.join(parentsList[-1], str(folderName))
                if os.path.exists(folderPath):
                    print('Error: At least one of the target folders already exists: {}'.format(folderPath))
                    sys.exit()
                parentsList.append(folderPath)
                os.mkdir(folderPath)
                # create an empty dirOrderFile under the new directory (for the next level)
                nextDirOrderFullFileName = os.path.join(folderPath, dirOrderFile)
                open(nextDirOrderFullFileName, 'w').close()
                dirOrderFullFileName = os.path.join(parentsList[-2], dirOrderFile)
                with open(dirOrderFullFileName, 'a') as fo:
                    fo.write('{}\n'.format(folderName))
                parentLevel = level
    except IOError as e:
        print('Operation failed: {}'.format(e.strerror))

def getFolderNameAndIndentLevel(line):
    """Validate line and return fileName and indentation level if valid, or None for fileName otherwise"""
    if not line.strip():                # skip lines with only whitespace
        return None, 0

    line = line.rstrip()                # remove trailing white spaces
    folderName = line.lstrip('\t')      # remove leading tabs
    level = len(line) - len(folderName) # level equals leading tabs count
    return folderName, level

def main():
    tocFullFileName = os.path.join(tocPath, tocFile)
    if not os.path.exists(tocFullFileName):
        print('Error: TOC file <{}> does not exist in <{}>'.format(tocFile, tocPath))
        sys.exit()

    try:
        with open(tocFullFileName, 'r') as fi:
            createDirectories(fi)
    except IOError as e:
        print('Error: Operation failed: {}'.format(e.strerror))

if __name__ == '__main__':
    main()