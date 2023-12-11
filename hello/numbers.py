firstMsg = "Hello World"
print(firstMsg)

plus= (4+4)
print(plus)

minus= (4-4)
print(minus)

mult= (4*4)
print(mult)

divs= (4/4)
print(divs)

ranEqs1= ((50 - 5*6) / 4)
print(ranEqs1)

classicDivs= (17 / 3) #classic division returns a float
print(classicDivs)
floorDivs= (17 // 3) # floor division discards the fractional part
print(floorDivs)
remainDivs= (17 % 3) # the % operator returns the remainder of the division
print(remainDivs)

sqrd= (5**2)
print(sqrd)

# The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

width = 20
height = 5 * 9
print(width * height)

# There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:
print(4 * 3.75 - 1)

# In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:
tax = 12.5 / 100
price = 100.50
print(price * tax)


 #price + _   113.06
 #113.0625
 #round(_, 2)
 #113.06

