# Ask a to enter three different integers
number1 = int(input("Enter your integer:"))
number2 = int(input("Enter your integer:"))
number3 = int(input("Enter your integer:"))

# sum of all numbers
sum_of_num = number1 + number2 + number3
print(sum_of_num)

# subtract first num and second num
subtract = number1 - number2
print(f"The sum of all the numbers is {sum_of_num}")
print(subtract)

# multipliy third num by the fist num
multiply = number3 * number1
print(f"{number3} * {number1} is {multiply}")

print(multiply)

# Divide the sum of all three numbers by third num
divide = (f"{number1} + {number2} + {number3} / {number3}")
print(divide)
