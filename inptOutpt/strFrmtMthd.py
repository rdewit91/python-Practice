#           ---         The String format() Method          ---

# Basic usage of the str.format() method looks like this:

print('we are the {} who say "{}!'.format('knights,', 'Ni'))

#The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

#If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.