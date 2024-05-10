#           ---         Old string formatting           ---

#The % operator (modulo) can also be used for string formatting. Given 'string' % values, instances of % in string are replaced with zero or more elements of values. This operation is commonly known as string interpolation. For example:

import math
print('The value of pi is approximately %5.3f.' % math.pi)
