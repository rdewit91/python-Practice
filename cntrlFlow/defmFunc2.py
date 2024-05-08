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

#When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you Have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#Note that the order in which the keyword arguments are printed is guaranteed to match the order in which they were provided in the function call

#Special parameters

#By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

#A function definition may look like:
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#      -----------    ----------     ----------
#        |             |                  |
#        |        Positional or keyword   |
#        |                                - Keyword only
#         -- Positional only

#where / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.

#If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.

#Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only. If positional-only, the parameters’ order matters, and the parameters cannot be passed by keyword. Positional-only parameters are placed before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the parameters. If there is no / in the function definition, there are no positional-only parameters.

#Parameters following the / may be positional-or-keyword or keyword-only.

#To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.

#Consider the following example function definitions paying close attention to the markers / and *:
def standard_arg(arg):
    print(arg)
    
def pos_only_arg(arg, /):
    print(arg)
    
def kwd_only_arg(*, arg):
    print(arg)
    
def combind_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
    
#The first function definition, standard_arg, the most familiar form, places no restrictions on the calling convention and arguments may be passed by position or keyword:

standard_arg(2)
standard_arg(arg=2)

#The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition:

pos_only_arg(1)
#pos_only_arg(arg=1) 
# File "<stdin>", line 1, in <module>
#TypeError: pos_only_arg() got some positional-only arguments passed as keyword #arguments: 'arg'

#The third function kwd_only_args only allows keyword arguments as indicated by a * in the function definition:

#kwd_only_arg(3)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
kwd_only_arg(arg=3)

#And the last uses all three calling conventions in the same function definition:

#combind_example(1, 2, 3)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: combined_example() takes 2 positional arguments but 3 were given
combind_example(1, 2, kwd_only=3)
combind_example(1, standard=2, kwd_only=3)
#combind_example(pos_only_arg=1, standard=2, kwd_only=3)
#traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: combined_example() got some positional-only arguments passed as keyword #arguments: 'pos_only'

#Finally, consider this function definition which has a potential collision between the positional argument name and **kwds which has name as a key:

#def foo(name, **kwds):
#    return 'name' in kwds

#There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter. For example:

#foo(1, **{'name' : 2})
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: foo() got multiple values for argument 'name'

#But using / (positional only arguments), it is possible since it allows name as a positional argument and 'name' as a key in the keyword arguments:

def foo(name, /, **kwds):
    print('name' in kwds)
#    return 'name' in kwds

foo(1, **{'name' : 2})

#The use case will determine which parameters to use in the function definition:

#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

#As guidance:

#Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

#Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.
#For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

#Arbitrary Argument Lists

#Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple. Before the variable number of arguments, zero or more normal arguments may occur.

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

#Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

def concat(*args, sep="/"):
    print (sep.join(args))
#    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

#npacking Argument Lists

#The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:

list(range(3,6))
#[3, 4, 5]
args = [3,6]
list(range(*args))
#[3, 4, 5]

#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#Lambda Expressions

#Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:

def make_incrementor(n):
#    print (lambda x: x + n)
    return lambda x: x + n

f = make_incrementor(42)
f(0)
#42
f(1)
#43


#The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#Documentation Strings

#Here are some conventions about the content and formatting of documentation strings.

#The first line should always be a short, concise summary of the object’s purpose. For brevity, it should not explicitly state the object’s name or type, since these are available by other means (except if the name happens to be a verb describing a function’s operation). This line should begin with a capital letter and end with a period.

#If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

#The Python parser does not strip indentation from multi-line string literals in Python, so tools that process documentation have to strip indentation if desired. This is done using the following convention. The first non-blank line after the first line of the string determines the amount of indentation for the entire documentation string. (We can’t use the first line since it is generally adjacent to the string’s opening quotes so its indentation is not apparent in the string literal.) Whitespace “equivalent” to this indentation is then stripped from the start of all lines of the string. Lines that are indented less should not occur, but if they occur all their leading whitespace should be stripped. Equivalence of whitespace should be tested after expansion of tabs (to 8 spaces, normally).

#Here is an example of a multi-line docstring:

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# Function Annotations

#Function annotations are completely optional metadata information about the types used by user-defined functions

#Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal ->, followed by an expression, between the parameter list and the colon denoting the end of the def statement. The following example has a required argument, an optional argument, and the return value annotated:

def f(ham: str, eggs: str ='eggs') -> str:
    print("Anotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')