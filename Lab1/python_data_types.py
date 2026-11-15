"""Create variables of several built-in Python data types."""

student_name = "Jhalak"
student_age = 20
student_height = 5.9
is_student = True

sample_values = {
    "Name": student_name,
    "Age": student_age,
    "Height": student_height,
    "Student status": is_student,
}

for description, value in sample_values.items():
    print(f"{description} Type: {type(value)}")
