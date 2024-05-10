#           ---         The String format() Method          ---

# Basic usage of the str.format() method looks like this:

print('we are the {} who say "{}!'.format('knights,', 'Ni'))

#The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

#If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.

print('this {food} is {adjective}.'.format(food='spam', adjective='absolutley horrible'))

#Positional and keyword arguments can be arbitrarily combined:

print('the story of {0}, {1}, and {other}'.format('bill', 'manfred0', other='george'))

#If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys.

table ={'Sjored': 4127, 'jack': 4098, 'Dcab': 8637678}
print('Jack: {0[jack]:d}; Sjored: {0[Sjored]:d}; Dcab: {0[Dcab]:d}'.format(table))

#This could also be done by passing the table dictionary as keyword arguments with the ** notation.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#This is particularly useful in combination with the built-in function vars(), which returns a dictionary containing all local variables.

#As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

for x in range (1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))