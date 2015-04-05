# Copyright PlatinumFactor.Com 2014
# Created Dec 12 2013
# This script creates a number of files of different sizes across many folders

import os
from sys import exit
import random
import shutil

size1 = int(input('Enter minimum size: '))
size2 = int(input('Enter maximum size: '))
totalFiles = int(input('Enter total number of files: '))
totalFolders = int(input('Enter total number of folders: '))

div1 = totalFiles%totalFolders

if div1 != 0:
	print("\n Files should be evenly divisible by folders. Please re-enter.\n ")
	exit(1)

filesindir = totalFiles/totalFolders

counter1 = 0
counter2 = 0

while counter1 < totalFolders:
	os.mkdir("/home/pfactor/dirs/folder" + str(counter1))
	counter1 += 1

randSize = random.randint(size1, size2)

while counter2 < totalFiles:
	c = 0
	f = open("/home/pfactor/files/file" + str(counter2), "wb")
	while c < randSize:
		f.write(bytes("e", 'UTF-8'))
		c += 1
	f.close()
	randSize = random.randint(size1, size2)
	counter2 += 1


files = os.listdir("/home/pfactor/files")
dirs = os.listdir("/home/pfactor/dirs")

b = 0

while b < len(dirs):
	a = 0
	while a < filesindir:
		shutil.move("/home/pfactor/files/" + files[a], "/home/pfactor/dirs/" + dirs[b])
		a += 1
	files = os.listdir("/home/pfactor/files")
	b += 1


