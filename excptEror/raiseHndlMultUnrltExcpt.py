#           ---         Raising and Handling Multiple Unrelated Exceptions

#There are situations where it is necessary to report several exceptions that have occurred. This is often the case in concurrency frameworks, when several tasks may have failed in parallel, but there are also other use cases where it is desirable to continue execution and collect multiple errors rather than raise the first exception.

#The builtin ExceptionGroup wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.

def f():
    excs = [OSError('error 1'), SyntaxError('error 2')]
    raise ExceptionGroup('there were problems', excs)

f()
#+ Exception Group Traceback (most recent call last):
#  |   File "<stdin>", line 1, in <module>
#  |   File "<stdin>", line 3, in f
#  | ExceptionGroup: there were problems
#  +-+---------------- 1 ----------------
#    | OSError: error 1
#    +---------------- 2 ----------------
#    | SystemError: error 2
#    +------------------------------------

try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')
    
#caught <class 'ExceptionGroup'>: e

#By using except* instead of except, we can selectively handle only the exceptions in the group that match a certain type. In the following example, which shows a nested exception group, each except* clause extracts from the group exceptions of a certain type while letting all other exceptions propagate to other clauses and eventually to be reraised.

def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
    
#There were OSErrors
#There were SystemErrors
#  + Exception Group Traceback (most recent call last):
#  |   File "<stdin>", line 2, in <module>
#  |   File "<stdin>", line 2, in f
#  | ExceptionGroup: group1
#  +-+---------------- 1 ----------------
#    | ExceptionGroup: group2
#    +-+---------------- 1 ----------------
#      | RecursionError: 4
#      +------------------------------------

#Note that the exceptions nested in an exception group must be instances, not types. This is because in practice the exceptions would typically be ones that have already been raised and caught by the program, along the following pattern:

excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)

if excs:
   raise ExceptionGroup("Test Failures", excs)