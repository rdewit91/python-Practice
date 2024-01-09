# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
for i in range(5):
    print(i)
    
#The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10. It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’):
exmpl1 = list(range(5, 10))
print(exmpl1)

exmpl2 = list(range(0, 10, 3))
print(exmpl2)

exmpl3 = list(range(-10, -100, -30))
print(exmpl3)

#To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
#In most such cases, however, it is convenient to use the enumerate() function,

#A strange thing happens if you just print a range:
#range(10)
#range(0, 10)
b = sum(range(4)) # 0 + 1 + 2 + 3
print(b)

#The break statement breaks out of the innermost enclosing for or while loop. A for or while loop can include an else clause.In a for loop, the else clause is executed after the loop reaches its final iteration. In a while loop, it’s executed after the loop’s condition becomes false. In either kind of loop, the else clause is not executed if the loop was terminated by a break. 
#This is exemplified in the following for loop, which searches for prime numbers:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
    else:
        print(n, 'is a prime number')
#Yes, this is the correct code. Look closely: the else clause belongs to the for loop, not the if statement

#When used with a loop, the else clause has more in common with the else clause of a try statement than it does with that of if statements: a try statement’s else clause runs when no exception occurs, and a loop’s else clause runs when no break occurs. 

#The continue statement, also borrowed from C, continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2== 0:
        print('Found an even number', num)
        continue
    print('Found an even number', num)
