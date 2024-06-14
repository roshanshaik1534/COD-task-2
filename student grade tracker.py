def student_grade_tracker():
    # Initialize variables
    total_grade = 0
    num_assignments = 0
    grades = []

    # Allow user to input grades for different subjects or assignments
    while True:
        assignment_grade = float(input("Enter the grade for an assignment (0 to quit): "))
        if assignment_grade == 0:
            break
        grades.append(assignment_grade)
        total_grade += assignment_grade
        num_assignments += 1

    # Calculate the average grade
    average_grade = total_grade / num_assignments

    # Display the overall grade along with additional information
    print("\nOverall Grade:", round(average_grade, 2))

    if average_grade >= 90:
        letter_grade = "A"
    elif average_grade >= 80:
        letter_grade = "B"
    elif average_grade >= 70:
        letter_grade = "C"
    elif average_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print("Letter Grade:", letter_grade)

    gpa = (average_grade - 50) / 10
    print("GPA:", round(gpa, 2))

# Call the student_grade_tracker function
student_grade_tracker()
