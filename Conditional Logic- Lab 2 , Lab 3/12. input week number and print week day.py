import datetime

def get_weekday(week_number):
    # Get the current year
    current_year = datetime.datetime.now().year

    # Create a datetime object for the first day of the specified week
    first_day = datetime.datetime.strptime(f'{current_year}-W{week_number}-1', "%Y-W%W-%w")

    # Get the weekday as an integer (Monday is 0 and Sunday is 6)
    weekday = first_day.weekday()

    # Define a list of weekday names
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Return the weekday name
    return weekdays[weekday]


# Main program
input_week = int(input("Enter a week number: "))

weekday = get_weekday(input_week)

print(f"The weekday for week {input_week} is {weekday}.")
