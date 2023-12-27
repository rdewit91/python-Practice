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