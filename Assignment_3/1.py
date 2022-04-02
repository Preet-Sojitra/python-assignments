#Input an integer, and print the multiplication table for the  number.

num = int(input("Enter an integer: "))

i=1

while i<=10:
    print(f"{num} X {i} = {num*i}")
    i +=1