'''
Created on Mar 2, 2015

@author: ds-ga-1007
'''

# Preliminary

NewDictionary= {'first':[2,1], 'second':[2,3], 'third':[3,4]}

# a. Swap the values of the first and third keys

NewDictionary = {'first':NewDictionary['third'], 'second':NewDictionary['second'], 'third':NewDictionary['first']}

#b. Sort the elements of the list with key third

NewDictionary['third'].sort()

#c. Add a new key fourth with the value of the key second

NewDictionary['fourth']=NewDictionary['second']

#d. Delete the key/value pair second

del NewDictionary['second']

print NewDictionary