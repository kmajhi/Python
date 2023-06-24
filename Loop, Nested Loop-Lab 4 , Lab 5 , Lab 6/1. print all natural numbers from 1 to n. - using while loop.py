def print_natural_numbers(n):
    num = 1
    while num <= n:
        print(num)
        num += 1

# Example usage:
n = int(input("Enter a value for n: "))
print("Natural numbers from 1 to", n)
print_natural_numbers(n)
