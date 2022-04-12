#Write a python program to read the admission number and names of 10 students from the keyboard. Create a dictionary of these admission number and names and ten display them on screen

i = 0
names_roll = []
while i < 10:
    admission_number = int(input("Enter admission number: "))
    name = input("Enter name: ")
    names_roll.append(f'{{"admission_number": {admission_number}, "name" : {name}}}')
    i += 1
print(names_roll)
