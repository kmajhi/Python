def calculate_electricity_bill(units):
    if units <= 50:
        total_bill = units * 0.50
    elif units <= 150:
        total_bill = 50 * 0.50 + (units - 50) * 0.75
    elif units <= 250:
        total_bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
    else:
        total_bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50
    
    surcharge = total_bill * 0.20  # 20% surcharge
    total_bill += surcharge
    
    return total_bill 


# Input electricity units from the user
units = int(input("Enter the electricity units: "))

# Calculate the total electricity bill
total_bill = calculate_electricity_bill(units)

# Print the result
print("Total electricity bill: Rs.", total_bill)
