number = int(input("Enter a number: "))
count = 0

# Handle the case of 0 separately since the logic below won't work for it
if number == 0:
    count = 1

while number != 0:
    number //= 10
    count += 1

print("The number of digits in the entered number is:", count)
