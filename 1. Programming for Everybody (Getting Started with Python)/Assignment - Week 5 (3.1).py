# Programming for Everybody (Getting Started with Python) by University of Michigan

# Assignment 3.1 (Week 5):
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate per hour:")
rph= float(rate)
if h<=40:
    total = h*rph
else:
    t1 = 40*rph
    t2 = (h-40)*(rph*1.5)
    total = t1+t2
print(total)

# Desired Output: 498.75