# Using Python to Access Web Data - University of Michigan

# Assignment - Week 2 (Ch.11): Extracting Data With Regular Expressions
# open file, search for numbers and sum them

import re

f_name = input( ' File name, only txt please = ', )
if len(f_name) < 1 :
    f_name = "regex_sum_1054991"
f = open(f_name + '.txt')
#print(f.read())

num = list() # list of integers
temp = list() 
value = 0

for line in f:
    #print (line)
    temp = re.findall( '[0-9]+' ,line) # [0-9]+ find all integers, the symbol '+' is for >1 int in one line 
    if len(temp) < 1 : continue
    #print(temp, line)
    for n in temp:
        value = value + 1 
        num.append( int(n) ) # string to integer, ''for loop'' for >1 int in one line

sumx = sum(num)

print('There are,',value,'values with a sum =',sumx)
out = input('Press enter to exit')

# Sum: 607896 for 'regex_sum_1054991' file
