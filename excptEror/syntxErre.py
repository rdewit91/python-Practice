#           ---         Syntax Errors           ---

#Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

#while true print('Hellow World')
#File "<stdin>", line 1
#    while True print('Hello world')
#               ^^^^^
#SyntaxError: invalid syntax

#The parser repeats the offending line and displays little ‘arrow’s pointing at the token in the line where the error was detected. The error may be caused by the absence of a token before the indicated token. In the example, the error is detected at the function print(), since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.