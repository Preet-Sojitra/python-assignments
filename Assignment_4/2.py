#2. Print the results of the arithmetic operation as shown:
# Adding 25 with 5. Ans: 30
# Subtracting 5 with 25. Ans: 20
# Multiplying 25 with 5. Ans: 125
# Dividing 25 with 5. Ans: 5

def operation(a,b):
    add = a + b
    sub = a-b
    mul = a*b
    div = a/b
    print('Addition is {0}, Subtraction is {1}, Multiplication is {2} and Division is {3}'.format(add,sub,mul,div))

a = 25
b = 5

operation(a,b)
