def sum_odd_numbers(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i
    return total

# Test the function
n = int(input("Enter a number: "))
sum_of_odd_numbers = sum_odd_numbers(n)
print("Sum of odd numbers between 1 and", n, "is:", sum_of_odd_numbers)
