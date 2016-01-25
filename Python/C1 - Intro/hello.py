"""
Input name and output a welcome message.

@author Hao Bin
@since 20140730
@modified 20140730
@param none
@precondition: User input a string
@postcondition:  Display a string of Hello [name]. Welcome
@complexity O(1)
"""

name = input('Enter name (max 60 chars): ')
#Accepts an input from the user and assign to variable name
print('Hello ' + name + '. Welcome')
#Prints out Hello [name] Welcome
