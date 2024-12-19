# Student grades dictionary
students_grades = {
    'Alice': 'A',
    'Bob': 'B',
    'Charlie': 'C',
    'David': 'B',
    'Eve': 'A'
}

# Display initial student grades
print("\nStudent grades:")
print(students_grades)

# Operations on student grades dictionary
students_grades['Frank'] = 'A'  # Add new student
students_grades['Charlie'] = 'B'  # Update student's grade
del students_grades['Eve']  # Remove student
print("\nUpdated student grades:", students_grades)
