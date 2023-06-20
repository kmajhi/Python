def get_days_in_month(month):
    if month == 2:  # February
        return 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # January, March, May, July, August, October, December
        return 31

month_number = int(input("Enter the month number (1-12): "))

if month_number < 1 or month_number > 12:
    print("Invalid month number!")
else:
    days = get_days_in_month(month_number)
    print(f"The number of days in month {month_number} is {days}.")
