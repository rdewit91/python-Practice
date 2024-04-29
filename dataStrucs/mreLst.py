#The list data type has some more methods. Here are all of the methods of list objects:

#list.append(x) Add an item to the end of the list. Equivalent to a[len(a):] = [x].

#list.extend(iterable) Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

#list.insert(i, x) Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

#list.remove(x) Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

#list.pop([i]) Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

#list.clear() Remove all items from the list. Equivalent to del a[:].

#list.index(x[, start[, end]]) Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

#list.count(x) Return the number of times x appears in the list.

#list.sort(*, key=None, reverse=False) Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

#list.reverse() Reverse the elements of the list in place.

#list.copy() Return a shallow copy of the list. Equivalent to a[:].

#An example that uses most of the list methods:

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana' ]
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

#You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. [1] This is a design principle for all mutable data structures in Python.

#Another thing you might notice is that not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types. Also, there are some types that don’t have a defined ordering relation. For example, 3+4j < 5+7j isn’t a valid comparison.

# Using Lists as Stacks

#The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. For example:

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)

#           ---         Using Lists as Queues           ---

#It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:

from collections import deque
queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")
print(queue)

queue.append("Graham")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

print(queue)

#           ---         List Comprehensions         ---

# List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

#For example, assume we want to create a list of squares, like:

squares = []
for x in range(10):
    squares.append(x**2)
    
print(squares)

# Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:

squares = list(map(lambda x : x**2, range(10)))
print(squares)

# or, equivalently:

squares = [x**8 for x in range(10)]
print(squares)

#which is more concise and readable.

#A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:

comb = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(comb)

# and it’s equivalent to:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
            
print(combs)

#Note how the order of the for and if statements is the same in both these snippets.

#If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
vecExmpl1 = [x*2 for x in vec]
print(vecExmpl1)

# filter the list to exclude negative numbers
vecExmpl2 = [x for x in vec if x >= 0]
print(vecExmpl2)

# apply a function to all the elements
vecExmpl3 = [abs(x) for x in vec]
print(vecExmpl3)

freshFruit = ["banana", "loganberry", "passion fruit"]

freshFruitExmpl1 = [weapon.strip() for weapon in freshFruit]
print(freshFruitExmpl1)

# create a list of 2-tuples like (number, square)
exmpl1 = [(x, x**2) for x in range(6)]
print(exmpl1)

# the tuple must be parenthesized, otherwise an error is raised
#[x, x**2 for x in range(6)]
#  File "<stdin>", line 1
#    [x, x**2 for x in range(6)]
#     ^^^^^^^
#SyntaxError: did you forget parentheses around the comprehension target?

# flatten a list using a listcomp with two 'for'
vec2 = [[1,2,3], [4,5,6], [7,8,9]]

vec2Exmpl1 = [num for elem in vec2 for num in elem]
print(vec2Exmpl1)

#List comprehensions can contain complex expressions and nested functions:

from math import pi
exmpl2 = [str(round(pi, i)) for i in range(1, 6)]
print(exmpl2)

#           ---         Nested List Comprehensions          ---

#The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension. Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

exampl3 = [[row[i] for row in matrix] for i in range(4)]
print(exampl3)

#As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it, so this example is equivalent to:

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#which, in turn, is the same as:

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

#In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:

transposed = list(zip(*matrix))
print(transposed)

#           ---         The del statement           ---         

# There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

#del can also be used to delete entire variables:

#           ---         Tuples and Sequences            ---

#We saw that lists and strings have many common properties, such as indexing and slicing operations. They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple. A tuple consists of a number of values separated by commas, for instance:

t = 12345, 54321, 'hello!'
print(t)
print(t[0])

u = t, (1, 2, 3, 4, 5)
print(u)

#t[0] = 88888
#print(t)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

v = ([1, 2, 3], [3, 2, 1])
print(v)

#As you see, on output tuples are always enclosed in parentheses, so that nested tuples are interpreted correctly; they may be input with or without surrounding parentheses, although often parentheses are necessary anyway (if the tuple is part of a larger expression). It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which contain mutable objects, such as lists.

#Though tuples may seem similar to lists, they are often used in different situations and for different purposes. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples). Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

#A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:

empty = ()
sigleton = 'hello', 
print(len(empty))

print(len(sigleton))

print(sigleton)

#The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345, 54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:

x, y, z = t

#This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side. Sequence unpacking requires that there are as many variables on the left side of the equals sign as there are elements in the sequence. Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.

#           ---         Sets            ---

#Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

#Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

#Here is a brief demonstration:

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')

print(a) # unique letters in a

print(a - b) # letters in a but not in b

print( a | b) # letters in a or b or both

print(a & b) # letters in both a and b
 
print(a ^ b) # letters in a or b but not both

#Similarly to list comprehensions, set comprehensions are also supported:

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#           ---         Dictionaries            ---

#Another useful data type built into Python is the dictionary (see Mapping Types — dict). Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

#It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

#The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

#Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

#Here is a small example using a dictionary:

tel = {'jack' : 4098, 'sape' : 4139}

tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)
print('jack' not in tel)

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:

dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)

#In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

dict2 = {x: x**2 for x in (2, 4, 6)}
print(dict2)

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:

dict3 = dict(sape=4139, guido=4127, jack=4098)
print(dict3)

#           ---         Looping Techniques          ---

# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    
# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
    
# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? it is {1}.' .format(q, a))
    
#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.

for i in reversed(range(1, 10, 2)):
    print(i)
    
#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.

bascket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
    
# Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
    
#It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

#           ---         More on Conditions          ---

#The conditions used in while and if statements can contain any operators, not just comparisons.

#The comparison operators in and not in are membership tests that determine whether a value is in (or not in) a container. The operators is and is not compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.

#Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.

#Comparisons may be combined using the Boolean operators and and or, and the outcome of a comparison (or of any other Boolean expression) may be negated with not. These have lower priorities than comparison operators; between them, not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C. As always, parentheses can be used to express the desired composition.

#The Boolean operators and and or are so-called short-circuit operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if A and C are true but B is false, A and B and C does not evaluate the expression C. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

#It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

string1, string2, string3 = '', 'Tronfheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator :=. This avoids a common class of problems encountered in C programs: typing = in an expression when == was intended.

#           ---         Comparing Sequences and Other Types         ---

#Sequence objects typically may be compared to other objects with the same sequence type. The comparison uses lexicographical ordering: first the first two items are compared, and if they differ this determines the outcome of the comparison; if they are equal, the next two items are compared, and so on, until either sequence is exhausted. If two items to be compared are themselves sequences of the same type, the lexicographical comparison is carried out recursively. If all items of two sequences compare equal, the sequences are considered equal. If one sequence is an initial sub-sequence of the other, the shorter sequence is the smaller (lesser) one. Lexicographical ordering for strings uses the Unicode code point number to order individual characters. Some examples of comparisons between sequences of the same type:

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

#Note that comparing objects of different types with < or > is legal provided that the objects have appropriate comparison methods. For example, mixed numeric types are compared according to their numeric value, so 0 equals 0.0, etc. Otherwise, rather than providing an arbitrary ordering, the interpreter will raise a TypeError exception.