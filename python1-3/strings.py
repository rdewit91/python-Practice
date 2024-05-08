#Python can manipulate text (represented by type str, so-called “strings”) as well as numbers. This includes characters “!”, words “rabbit”, names “Paris”, sentences “Got your back.”, etc. “Yay! :)”. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result
txt11= 'spam eggs'
print(txt11)
txt12= "Paris rabbit got your back :) Yay!"
print(txt12)
txt13= '\'Yes\' they said.'
print(txt13)
txt14= '"Isnt\'t," they said.'
print(txt14) 

#To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks:
txt21= 'doesn\'t' # use \' to escape the single quote...
txt22= "doesn\'t" # ...or use double quotes instead
txt23= '"Yes," they said.'
txt24= "\"Yes,\" they said."
txt25= '"Isnt\'t," they said'
print(txt21, txt22, txt23, txt24, txt25)

#In the Python shell, the string definition and output string can look different. The print() function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:
txt31= 'First Line. \nSecond line.' # \n means newline
# without print(), special characters are included in the string
'First line.\nSecond line.'
print(txt31) # with print(), special characters are interpreted, so \n produces new line

#If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
print('C:\some\name') # here \n means newline!
print(r'C:\some\name') # note the r before the quote

#There is one subtle aspect to raw strings: a raw string may not end in an odd number of \ characters; see the FAQ entry for more information and workarounds. String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'ium')

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py''thon')

#This feature is particularly useful when you want to break long strings:
print('Put several strings within parentheses '
        'to have them joined together.')

prefix = 'Py'
print(prefix + 'thon')

#Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
word= 'python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-2])
print(word[-6])

#In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain a substring:
print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[2:5]) # characters from position 2 (included) to 5 (excluded)

#Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end

#Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
print(word[:4] + word[4:])

#One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
#+---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1
#The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.
#For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

#Attempting to use an index that is too large will result in an error:
#print(word[42]) # the word only has 6 characters
#IndexError: string index out of range

#However, out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42])
print(word[42:])

#Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
#word[0] = 'J'
#raceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'str' object does not support item assignment
#word[2:] = 'py'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'str' object does not support item assignment

#If you need a different string, you should create a new one:
print('J' + word[1:])
print(word[:2] + 'py')

#The built-in function len() returns the length of a string:
s= 'supercalifragilisticexpialidocious'
print(len(s))