"""Student marks manager: maintain student records and generate class reports."""

student_records = {
    101: {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chemistry": 92}},
    102: {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chemistry": 64}},
    103: {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chemistry": 69}},
}


def get_valid_mark():
    """Read a mark in the inclusive range 0 to 100."""
    while True:
        try:
            value = float(input("Enter marks (0-100): "))
            if 0 <= value <= 100:
                return value
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric mark.")


def add_student():
    roll_number = int(input("Enter roll number: "))
    if roll_number in student_records:
        print("This roll number already exists.")
        return

    student_name = input("Enter student name: ").strip()
    if not student_name:
        print("Name cannot be empty.")
        return

    subject_scores = {}
    subject_count = int(input("Enter number of subjects: "))
    if subject_count <= 0:
        print("Enter at least one subject.")
        return

    for _ in range(subject_count):
        subject_name = input("Enter subject name: ").strip()
        if subject_name:
            subject_scores[subject_name] = get_valid_mark()

    student_records[roll_number] = {
        "name": student_name,
        "marks": subject_scores,
    }
    print("Student record added.")


def update_marks():
    roll_number = int(input("Enter roll number: "))
    if roll_number not in student_records:
        print("Student not found.")
        return

    subject_name = input("Enter subject name: ").strip()
    if not subject_name:
        print("Subject name cannot be empty.")
        return

    student_records[roll_number]["marks"][subject_name] = get_valid_mark()
    print("Marks updated.")


def delete_student():
    roll_number = int(input("Enter roll number: "))
    if roll_number in student_records:
        del student_records[roll_number]
        print("Record deleted.")
    else:
        print("Student not found.")


def search_student():
    roll_number = int(input("Enter roll number: "))
    record = student_records.get(roll_number)
    if record is None:
        print("Student not found.")
    else:
        print(record)


def display_reports():
    averages = {}
    for roll_number, record in student_records.items():
        score_values = record["marks"].values()
        if score_values:
            averages[roll_number] = sum(score_values) / len(record["marks"])

    print("\nAverage marks:")
    for roll_number, average in averages.items():
        print(student_records[roll_number]["name"], ":", round(average, 2))

    if averages:
        top_roll = max(averages, key=averages.get)
        print("Class topper:", student_records[top_roll]["name"])

    subject_leaders = {}
    for record in student_records.values():
        for subject, score in record["marks"].items():
            current = subject_leaders.get(subject)
            if current is None or score > current[1]:
                subject_leaders[subject] = (record["name"], score)

    print("\nHighest scorer in each subject:")
    for subject, (name, score) in subject_leaders.items():
        print(subject, ":", name, "-", score)

    print("\nStudents scoring below 40:")
    any_low_scores = False
    for record in student_records.values():
        below_threshold = {
            subject: score
            for subject, score in record["marks"].items()
            if score < 40
        }
        if below_threshold:
            print(record["name"], ":", below_threshold)
            any_low_scores = True
    if not any_low_scores:
        print("None")

    grade_groups = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for roll_number, average in averages.items():
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"
        grade_groups[grade].append(student_records[roll_number]["name"])

    print("\nGrade-wise list:")
    print(grade_groups)


def main():
    while True:
        print("\n--- STUDENT DATABASE ---")
        print("1. Add student")
        print("2. Update marks")
        print("3. Delete student")
        print("4. Search student")
        print("5. Display reports")
        print("6. Exit")

        option = input("Choose an option: ")
        if option == "1":
            add_student()
        elif option == "2":
            update_marks()
        elif option == "3":
            delete_student()
        elif option == "4":
            search_student()
        elif option == "5":
            display_reports()
        elif option == "6":
            print("Program closed.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
