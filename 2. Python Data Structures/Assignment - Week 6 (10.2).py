# Python Data Structures - University of Michigan

# Assignment - Week 6:
# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 5:
            time_all = words[5] # 09:14:16
            split_time = time_all.split(":") # ['09', '14', '16']
            hour = split_time[0] # 09
            counts[hour]=counts.get(hour,0)+1

lst = list()
for key,val in counts.items():
    lst.append( (key,val) ) # ('09', 2)

lst = sorted(lst) # sort by key s2b

for key,val in lst:
    print(key,val)


# Desired Output: 
# 
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1