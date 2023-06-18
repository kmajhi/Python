def check_divisibility(number):
    if number % 5 == 0 and number % 11 == 0:
        print(f"{number} is divisible by 5 and 11.")
    else:
        print(f"{number} is not divisible by both 5 and 11.")

# Example usage
num = int(input("Enter a number: "))
check_divisibility(num)
