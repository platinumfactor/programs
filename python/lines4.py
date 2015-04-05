# This script merges two files line by line

file1 = open("linesfile1.txt", "r")
file2 = open("linesfile2.txt", "r")
linesoffile1 = file1.readlines()
linesoffile2 = file2.readlines()

x = len(linesoffile1)

a=0
while a < x:
  print(linesoffile1[a])
  print(linesoffile2[a])
  a += 1
