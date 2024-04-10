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