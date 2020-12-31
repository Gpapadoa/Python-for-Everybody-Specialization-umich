# Python Data Structures - University of Michigan

# Assignment - Week 5:
# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic_mail = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        for word in words:
            if '@' in word:
                dic_mail[word] = dic_mail.get(word,0)+1
                
                
count_max = 0
for word,count in dic_mail.items():
    if count > count_max:
        word_max = word
        count_max = count
        
print(word_max, count_max)

# Desired Output: cwen@iupui.edu 5