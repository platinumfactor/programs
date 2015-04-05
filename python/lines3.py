# This script merges two files line by line

file1 = open("linesfile1.txt", "r")
file2 = open("linesfile2.txt", "r")

for l1, l2 in zip(file1, file2):
    print(l1+l2)
