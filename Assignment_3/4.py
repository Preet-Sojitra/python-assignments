#Input a float number which will be the side of a square,  prompt user to enter a positive value if user inputs a  negative value. Finally calculate the area of the square.  (Hint : use “continue”)

side = float(input("Enter side of square: "))
while True:
    if side > 0:
        area = side * side
        print("Area of square is: ", area)
        break
    else:
        print("Please enter positive value")
        side = float(input("Enter side of square: "))
        continue
    
    

    