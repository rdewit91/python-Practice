#           ---         Methods of File Objects         ---

#The rest of the examples in this section will assume that a file object called f has already been created.

#To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise, at most size characters (in text mode) or size bytes (in binary mode) are read and returned. If the end of the file has been reached, f.read() will return an empty string ('').

#f.read()
'This is the entire file.\n'
#f.read()
''

#f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

#f.readline()
'This is the first line of the file.\n'
#f.readline()
'Second line of the file\n'
#f.readline()

#For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

#for line in f:
#    print(line, end='')
#This is the first line of the file.
#second line of the file

#If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

#f.write(string) writes the contents of string to the file, returning the number of characters written.

#f.write('This is a test\n')
#15
#Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

#value = ('the answer', 42)
#s = str(value)  # convert the tuple to string
#f.write(s)
#18

#f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

#To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

#f = open('workfile', 'rb+')
#f.write(b'0123456789abcdef')
#16
#f.seek(5)      # Go to the 6th byte in the file
#5
#f.read(1)
#b'5'
#f.seek(-3, 2)  # Go to the 3rd byte before the end
#13
#f.read(1)
#b'd'