# createTOC.py
# MIT license; Copyright (C) 2018 Uri Benchetrit

"""Traverse a directory tree and generate an ordered linked validated TOC.

Usage:
  createTOC.py [options] [FILE]

Arguments:
  FILE  destination TOC filename

Options:
  -h --help             show this help message and exit
  -v --verbose          print warning messages
  --dirs-root=PATH      directories tree root relative to program location [default: ../Training/] 
  --toc-path=PATH       TOC file path relative to program location [default: ../]
  --links-root=PATH     TOC file links root relative to TOC file location [default: ./Training/]
  -d --depth=LEVEL      max depth of the generated TOC tree [default: 8]
  --start-index=INDEX   start index of the TOC items [default: 1]
  --no-item-prefix      do not include item prefix for the TOC items
  --no-index            do not include index numbers for the TOC items
  --no-item-link        do not include links for the TOC items
  --header              include HTML header for the TOC file
"""

from docopt import docopt
import os
import sys
from urllib.request import pathname2url

tocFile = 'TOC.md'
tocHeader = '<style>ul { list-style-type: none; }</style>\n\n'  # kill bullets of unordered list
tocTitle = '## Table of Contents\n\n'
markdownUL = '-'
dirOrderFile = '.dirorder'
whiteList = ['.md']
blackList = [dirOrderFile, tocFile, sys.argv[0]]

def createTOC(path, tocFileObject, level, index):
    """"""
    if level >= maxDepth:
        return

    dirOrderFileList = dirOrderFileToList(path)
    fileList = os.listdir(path)
    fileList = filterFiles(path, fileList)
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

def filterFiles(path, fileList):
    """"""
    ignoreList = []
    for fileName in fileList:
        filePath = os.path.join(path, fileName)
        if not os.path.isdir(filePath):
            extension = os.path.splitext(fileName)[1]
            if extension not in whiteList:
                ignoreList.append(fileName)

    return list(set(fileList) - set(ignoreList + blackList))

def dirOrderFileToList(path):
    """"""
    try:
        dirOrderFullFileName = os.path.join(path, dirOrderFile)
        if not os.path.exists(dirOrderFullFileName):
            # allow missing dirOrderFile for an empty directory 
            # note: be aware that git is a content tracker and empty directories are not content
            if verbose and not os.listdir():
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
        fileLink = filePath.replace(dirsTreeRoot, tocLinksRoot)
        fileLinkURL = pathname2url(fileLink)
        tocItem = '[' + fileName + '](' + fileLinkURL + ')'

    return '{}{}{}{}\n'.format(indent, itemPrefix, indexString, tocItem)

def processArgs():
    global verbose, maxDepth, startIndex, includeItemPrefix, includeIndex
    global includeItemLink, includeTocHeader, whiteList, blackList
    global dirsTreeRoot, tocPath, tocLinksRoot, tocFile

    args = docopt(__doc__)

    print(args)

    verbose = args['--verbose']
    maxDepth = int(args['--depth'])
    startIndex = int(args['--start-index'])
    includeItemPrefix = not args['--no-item-prefix']
    includeIndex = not args['--no-index']
    includeItemLink = not args['--no-item-link']
    includeTocHeader = args['--header']
    dirsTreeRoot = args['--dirs-root']
    tocPath = args['--toc-path']
    tocLinksRoot = args['--links-root']

    if args['FILE'] is not None:
        tocFile = args['FILE']

def main():
    tocFullFileName = os.path.join(tocPath, tocFile)
    if os.path.exists(tocFullFileName):
        print('Error: TOC file <{}> already exists in <{}>'.format(tocFile, tocPath))
        sys.exit()

    try:
        with open(tocFullFileName, 'a') as fo:
            if includeTocHeader:
                fo.write(tocHeader)
            fo.write(tocTitle)
            root = dirsTreeRoot
            level = 0
            index = [startIndex]
            createTOC(root, fo, level, index)
    except IOError as e:
        print('Error: Operation failed: {}'.format(e.strerror))

if __name__ == '__main__':
    processArgs()
    main()