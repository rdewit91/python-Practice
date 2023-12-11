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
