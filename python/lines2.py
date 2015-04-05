# This script merges two files line by line

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

for lineinfile1, lineinfile2 in zip(file1, file2):
    # print(line + file2.readline())
    print (lineinfile1 + lineinfile2)