def calculate_sum(n):
    if n < 1:
        return 0

    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i

    return total_sum

# Get input from the user
n = int(input("Enter a number: "))

# Calculate the sum of natural numbers
sum_of_natural_numbers = calculate_sum(n)

# Display the result
print("The sum of natural numbers from 1 to", n, "is:", sum_of_natural_numbers)
