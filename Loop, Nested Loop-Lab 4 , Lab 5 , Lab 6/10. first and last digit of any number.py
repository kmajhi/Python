number = int(input("Enter a number: "))

first_digit = int(str(number)[0])
last_digit = number % 10

print("First digit:", first_digit)
print("Last digit:", last_digit)
