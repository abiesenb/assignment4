'''
Created on Mar 2, 2015

@author: ds-ga-1007
'''

# Get the input from the user. Here I just did the same process as in the HW question.

FirstName = raw_input("Enter your first name: ")
LastName  = raw_input("Enter your last name: ")
print "Enter your date of birth: "
Month = raw_input("Month (in string form, e.g. 'January')? ")  
Day = raw_input("Day (as a number)? ")
Year = raw_input("Year (as a number)? ")

# Print the formatted results, as done in the HW question. 

print  FirstName + " " + LastName + " was born on " + Month + " " + Day + ", " + Year + "."