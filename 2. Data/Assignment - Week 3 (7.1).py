# Python Data Structures - University of Michigan

# Assignment - Week 3:
# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line_new= line.upper().rstrip()
    print(line_new)


# Desired Output: words.txt but all in capital