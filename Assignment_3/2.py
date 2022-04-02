#Input 10 characters using while loop and count how many vowels are there.

count = 0
i = 1
while i<=10:
    chars = input("Enter a character: ")
    if chars == "a" or chars == "e" or chars == "i" or chars == "o" or chars == "u":
        count +=1
    i += 1
print(f"There are {count} vowels")
    