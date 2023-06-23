def calculate_gross_salary(basic_salary):
    if basic_salary <= 10000:
        hra = basic_salary * 0.2
        da = basic_salary * 0.8
    elif basic_salary <= 20000:
        hra = basic_salary * 0.25
        da = basic_salary * 0.9
    else:
        hra = basic_salary * 0.3
        da = basic_salary * 0.95

    gross_salary = basic_salary + hra + da
    return gross_salary


# Input basic salary from the user
basic_salary = float(input("Enter the basic salary: "))

# Calculate the gross salary
gross_salary = calculate_gross_salary(basic_salary)

# Print the result
print("Gross salary:", gross_salary)
