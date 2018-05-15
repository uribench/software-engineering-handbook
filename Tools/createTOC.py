# createTOC.py
# Traverse a directory tree and generate an ordered linked validated TOC

import os
import sys
from urllib.request import pathname2url

targetRoot = '.' + os.sep
tocFile = 'TOC.md'
tocHeader = '<style>ul { list-style-type: none; }</style>\n\n'  # kill bullets of unordered list
tocTitle = '### Table of Content\n\n'
markdownUL = '-'
dirOrderFile = '.dirorder'
whileList = ['.md']
blackList = [dirOrderFile, tocFile, sys.argv[0]]
tocMaxLevel = 8
initialIndex = 1
includeIndex = True
includeItemPrefix = True
includeItemLink = True
displayWarnings = True

def createTOC(path, tocFileObject, level, index):
    """"""
    if level >= tocMaxLevel:
        return

    dirOrderFileList = dirOrderFileToList(path)
    fileList = os.listdir(path)
    fileList = filterFiles(path, fileList, whileList)
    if not validateIntegrity(path, dirOrderFileList, fileList):
        sys.exit()

    # dirOrderFile exists, is not empty, and matches the directory content, use it to force listing order
    if dirOrderFileList:
        fileList = dirOrderFileList        

    for fileName in fileList:
        tocFileObject.write(formatTOC(path, fileName, level, index))
        filePath = os.path.join(path, fileName)
        if os.path.isdir(filePath):
            createTOC(filePath, tocFileObject, level + 1, index + [1])
        index[level] += 1

def filterFiles(path, fileList, whileList):
    """"""
    ignoreList = []
    for fileName in fileList:
        filePath = os.path.join(path, fileName)
        if not os.path.isdir(filePath):
            extension = os.path.splitext(fileName)[1]
            if extension not in whileList:
                ignoreList.append(fileName)

    return list(set(fileList) - set(ignoreList + blackList))

def dirOrderFileToList(path):
    """"""
    try:
        dirOrderFullFileName = os.path.join(path, dirOrderFile)
        if not os.path.exists(dirOrderFullFileName):
            # allow missing dirOrderFile for an empty directory 
            # note: be aware that git is a content tracker and empty directories are not content
            if displayWarnings and not os.listdir():
                print('Warning: Expected <{}> file does not exit in <{}>'.format(dirOrderFile, path))
            return []

        return [line.rstrip() for line in open(dirOrderFullFileName, 'r')]

    except IOError as e:
        print('Error: Operation failed: {}'.format(e.strerror))
        sys.exit()

def validateIntegrity(path, dirOrderFileList, fileList):
    """"""
    # allow missing or empty dirOrderFile for an empty directory
    # note: be aware that git is a content tracker and empty directories are not content
    if not dirOrderFileList and not fileList:
        return True

    isValid = True
    diffList = list(set(dirOrderFileList) - set(fileList))
    if diffList:
        print('Error: Based on <{}>, directory <{}> is missing the following content: {}'.format(path, dirOrderFile, diffList))
        isValid = False

    diffList = list(set(fileList) - set(dirOrderFileList))
    if diffList:
        print('Error: Based on the content of directory <{}>, <{}> is missing the following content: {}'.format(path, dirOrderFile, diffList))
        isValid = False

    return isValid

def formatTOC(path, fileName, level, index):
    """"""
    # compose indent string
    indent = ' ' * 4 * level
    # compose optional index string
    # list('-'.join(ls))
    # str1 = ''.join(str(e) for e in list1)
    indexString = ''
    if includeIndex:
        indexString = '.'.join(str(e) for e in index[:level + 1])
        indexString += ' '
    # compose optional item prefix string
    itemPrefix = ''
    if includeItemPrefix:
        itemPrefix = markdownUL + ' '
    # compose item string with optional link
    tocItem = fileName
    if includeItemLink:
        filePath = os.path.join(path, fileName)
        filePathURL = pathname2url(filePath)
        tocItem = '[' + fileName + '](' + filePathURL + ')'

    return '{}{}{}{}\n'.format(indent, itemPrefix, indexString, tocItem)

def main():
    if os.path.exists(tocFile):
        print('Error: TOC file <{}> already exists'.format(tocFile))
        sys.exit()

    try:
        with open(tocFile, 'a') as fo:
            fo.write(tocHeader)
            fo.write(tocTitle)
            root = targetRoot
            level = 0
            index = [initialIndex]
            createTOC(root, fo, level, index)
    except IOError as e:
        print('Error: Operation failed: {}'.format(e.strerror))

if __name__ == '__main__':
    main()