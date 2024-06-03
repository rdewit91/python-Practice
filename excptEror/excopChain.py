#           ---         Exception Chaining          ---

#If an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message:

try:
    open("database.splite")
except OSError:
    raise RecursionError("unable to handle error")

#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

#During handling of the above exception, another exception occurred:

#Traceback (most recent call last):
#  File "<stdin>", line 4, in <module>
#RuntimeError: unable to handle error

#To indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

# exc must be exception instance or None.
#raise RuntimeError from exc

def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RecursionError('Failed to open database') from exc

#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#  File "<stdin>", line 2, in func
#ConnectionError

#The above exception was the direct cause of the following exception:

#Traceback (most recent call last):
#  File "<stdin>", line 4, in <module>
#RuntimeError: Failed to open database

#It also allows disabling automatic exception chaining using the from None idiom:

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

#Traceback (most recent call last):
#  File "<stdin>", line 4, in <module>
#RuntimeError