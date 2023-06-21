def check_triangle_validity(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

# Take input from the user for the sides of the triangle
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Check the validity of the triangle
if check_triangle_validity(a, b, c):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
