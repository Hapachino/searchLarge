#! python3
# searchLarge.py
# find all files that are larger than 1 MB (1,048,576 bytes)
# and print to screen with absolute folder path

import os, sys

def searchLarge(folder):
	
    # Make sure folder is absolute path
    folder = os.path.abspath(folder)

    # create empty list
    matchList = []

    fileSize = 1048576

    # Walk down directory tree and add to list files larger then 1 MB
    for root, dirs, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(os.path.join(root, filename)) > fileSize:
                matchList.append(os.path.join(root, filename))

    # If no file is larger than 1 MB, print to screen and exit program
    if len(matchList) < 1:
        print('No file larger than 1 MB found.')
        sys.exit()

    # print to screen all files in list
    for filename in matchList:
        print(filename)
