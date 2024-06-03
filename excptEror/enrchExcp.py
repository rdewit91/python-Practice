#           ---         Enriching Exceptions with Notes         ---

#When an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred. There are cases where it is useful to add information after the exception was caught. For this purpose, exceptions have a method add_note(note) that accepts a string and adds it to the exception’s notes list. The standard traceback rendering includes all notes, in the order they were added, after the exception.

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#TypeError: bad type
#Add some information
#Add some more information

#For example, when collecting exceptions into an exception group, we may want to add context information for the individual errors. In the following each exception in the group has a note indicating when this error has occurred.

def f():
    raise OSError('operation failed')

excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)

#raise ExceptionGroup('We have some problems', excs)
#  + Exception Group Traceback (most recent call last):
#  |   File "<stdin>", line 1, in <module>
#  | ExceptionGroup: We have some problems (3 sub-exceptions)
#  +-+---------------- 1 ----------------
#    | Traceback (most recent call last):
#    |   File "<stdin>", line 3, in <module>
#    |   File "<stdin>", line 2, in f
#    | OSError: operation failed
#   | Happened in Iteration 1
#    +---------------- 2 ----------------
#    | Traceback (most recent call last):
#    |   File "<stdin>", line 3, in <module>
#    |   File "<stdin>", line 2, in f
#    | OSError: operation failed
#    | Happened in Iteration 2
#    +---------------- 3 ----------------
#    | Traceback (most recent call last):
#    |   File "<stdin>", line 3, in <module>
#    |   File "<stdin>", line 2, in f
#    | OSError: operation failed
#    | Happened in Iteration 3
#    +------------------------------------