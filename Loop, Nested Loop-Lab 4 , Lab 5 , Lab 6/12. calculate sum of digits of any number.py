number = int(input("Enter a number: "))
sum_of_digits = 0

# Take the absolute value of the number to handle negative numbers
number = abs(number)

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("The sum of digits in the entered number is:", sum_of_digits)
