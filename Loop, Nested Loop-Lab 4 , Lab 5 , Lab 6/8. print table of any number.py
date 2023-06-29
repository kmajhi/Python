def print_table(number, limit):
    for i in range(1, limit + 1):
        product = number * i
        print(f"{number} x {i} = {product}")

# Test the function
number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
print_table(number, limit)
