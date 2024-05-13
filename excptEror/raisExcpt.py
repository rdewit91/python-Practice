#           ---         Raising Exceptions          ---

#The raise statement allows the programmer to force a specified exception to occur. For example:

#raise NameError('HiThere')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: HiThere

#The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

#raise ValueError

#If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception:

try:
    raise NameError('Hi There')
except NameError:
    print('An exception flew by!')
    raise