'''
Created on Mar 2, 2015

@author: ds-ga-1007
'''

"""
Start with the list [1, 2, 3, 4, 5, 6, 7, 8, 9]. 
Using list slicing and the list operator functions 
(append, sort, etc.) only, what is the shortest series
of statements you can find that transform this list into 
a list containing the following elements?

[1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
"""

ListOne = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9][0:4]*4)
ListOne.remove(2)
print ListOne
