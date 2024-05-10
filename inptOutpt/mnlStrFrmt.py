#           ---         Manual String Formatting            ---

#Here’s the same table of squares and cubes, formatted manually:

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
    
#(Note that the one space between each column was added by the way print() works: it always adds spaces between its arguments.)

#The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative, which would be lying about a value. (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

#There is another method, str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs:

print('12' .zfill(5))
print('-3.14' .zfill(7))
print('3.14159265359' .zfill(5))