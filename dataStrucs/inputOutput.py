#           ---         Input and Output            ---

#There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use. This chapter will discuss some of the possibilities.

#           ---         Fancier Output Formatting           ---

#So far we’ve encountered two ways of writing values: expression statements and the print() function. (A third way is using the write() method of file objects; the standard output file can be referenced as sys.stdout. See the Library Reference for more information on this.)

#Often you’ll want more control over the formatting of your output than simply printing space-separated values. There are several ways to format output.

#To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

year = 2016
event = "Referendum"
print(f'Result of {year} {event}')

#The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))