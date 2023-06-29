def sum_of_even_numbers(n):
    sum = 0
    for num in range(2, n + 1, 2):
        sum += num
    return sum

# Example usage
n = int(input("Enter a number: "))
result = sum_of_even_numbers(n)
print(f"The sum of even numbers between 1 and {n} is: {result}")
