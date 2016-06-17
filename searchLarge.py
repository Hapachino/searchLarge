#! python3
# searchLarge.py
# find all files that are larger than 100 MB (1,048,576 bytes)
# and print to screen with absolute folder path

import os

def searchLarge(folder):
	
	# Make sure folder is absolute path
	folder = os.path.abspath(folder)
	
	# create empty list
	matchList = []

	fileSize = 1048576
	
	# Walk down directory tree and add to list files larger then 1MB
	for root, dirs, filenames in os.walk(folder):
		for filename in filenames:
			if os.path.getsize(os.path.join(folder, filename)) > fileSize:
			  matchList.append(os.path.join(folder, filename))

	# print to screen all files in list
	for filename in matchList:
		print(filename)
	


