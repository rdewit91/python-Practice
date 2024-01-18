#It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

#Default Argument Values
#The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow. For example:

def ask_ok(promt, retries=4, reminder="Please Try Again!"):
    while True:
        reply = input(promt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)
#This function can be called in several ways:

#giving only the mandatory argument: ask_ok('Do you really want to quit?')
#giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
#or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

#This example also introduces the in keyword. This tests whether or not a sequence contains a certain value.

#The default values are evaluated at the point of function definition in the defining scope, so that
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
#will print 5.
#Important warning: The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:
def parrot(voltage, state='a stiff', action='voom', type='Noregion Blue'):
    print('-- This parrot wouldnt', action, end=' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print('-- its', state, '!')
    
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#but all the following calls would be invalid:

#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument

#In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function (e.g. actor is not a valid argument for the parrot function), and their order is not important. This also includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may receive a value more than once. Here’s an example that fails due to this restriction:

#def function(a):
#    pass

#function(0, a=0)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: function() got multiple values for argument 'a'

