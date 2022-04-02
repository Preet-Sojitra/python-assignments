#Find sum of numbers from 1 to 100 which are divisible by either 2 or3. (Hint : use while loop + compound if statement -“or”)

sum = 0
i = 1
while i<=100:
    if i%2 == 0 or i%3 == 0:
        sum = sum + i
    i += 1
print("Sum is: ", sum)