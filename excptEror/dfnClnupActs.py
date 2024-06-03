#           ---         Defining Clean-up Actions           ---

#The try statement has another optional clause which is intended to define clean-up actions that must be executed under all circumstances. For example:

#try:
#    raise KeyboardInterrupt
#finally:
#    print('Goodbye, world!')

#Goodbye, world!
#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#KeyboardInterrupt

#If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception. The following points discuss more complex cases when an exception occurs:

#If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

#An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.

#If the finally clause executes a break, continue or return statement, exceptions are not re-raised.

#If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

#If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())
    
#A more complicated example:

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("result is", result)
    finally:
        print("executin finally clause")
        
print(divide(2, 1))
print(divide(2, 0))
print(divide("2", "1"))

#As you can see, the finally clause is executed in any event. The TypeError raised by dividing two strings is not handled by the except clause and therefore re-raised after the finally clause has been executed.

#In real world applications, the finally clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.