def check_triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or c == a:
        return "Isosceles"
    else:
        return "Scalene"

# Take input from the user for the sides of the triangle
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Check the type of the triangle
triangle_type = check_triangle_type(a, b, c)

# Print the type of the triangle
print("The triangle is", triangle_type, "triangle.")
