#           ---         Formatted String Literals           ---

# Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

#An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:

import math
print(f'the value of pi is approoximately {math.pi:.3f}.')

#Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

table = {'Sjoerd': 4127, 'Jack': 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    
#Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():

animals = 'eels'
print(f'my overcraft is full of {animals}.')
print(f'my overcraft is full of {animals!r}.')

#The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

bugs = 'roaches'
count = 13
area = 'living room'
print(f'debugging {bugs=} {count=} {area=}')