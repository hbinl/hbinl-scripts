"""
Converts a Celsius temperature to Fahrenheit scale.

@author Hao Bin
@since 20140730
@modified 20140730
@param none
@precondition: User inputs an integer
@postcondition:  An integer showing temperature in Fahrenheit
@complexity O(1)
"""

#Accepts an integer in Celsius
temp_C = int(input('Enter temperature in Celsius '))

#Converts the integer to Fahrenheit
temp_F = int(9*temp_C/5 + 32)

print('Temperature in Fahrenheit is ' + str(temp_F))
