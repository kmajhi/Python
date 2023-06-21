def calculate_percentage(marks):
    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    return percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >= 70:
        return "Grade C"
    elif percentage >= 60:
        return "Grade D"
    elif percentage >= 40:
        return "Grade E"
    else:
        return "Grade F"

# Take input from the user for the marks of five subjects
marks = []
subjects = ["Physics", "Chemistry", "Biology", "Mathematics", "Computer"]
for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

# Calculate the percentage
percentage = calculate_percentage(marks)

# Calculate the grade
grade = calculate_grade(percentage)

# Print the percentage and grade
print("Percentage:", percentage)
print("Grade:", grade)
