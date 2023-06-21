import cmath

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Calculate the roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2

# Take input from the user for the coefficients of the quadratic equation
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

# Find the roots of the quadratic equation
roots = find_roots(a, b, c)

# Print the roots
print("The roots of the quadratic equation are:")
print("Root 1:", roots[0])
print("Root 2:", roots[1])
