def find_maximum(num1, num2, num3):
    max_num = num1

    if num2 > max_num:
        max_num = num2

    if num3 > max_num:
        max_num = num3

    return max_num


# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

maximum = find_maximum(num1, num2, num3)
print("The maximum number is:", maximum)
