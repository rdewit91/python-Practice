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