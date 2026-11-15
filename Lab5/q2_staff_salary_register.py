"""Staff salary manager: maintain employee details and prepare salary reports."""

staff_records = {
    "E01": {"name": "Kiran", "department": "IT", "salary": 60000},
    "E02": {"name": "Sara", "department": "HR", "salary": 45000},
    "E03": {"name": "Dev", "department": "IT", "salary": 75000},
    "E04": {"name": "Nina", "department": "Finance", "salary": 52000},
    "E05": {"name": "Omar", "department": "HR", "salary": 48000},
}


def add_employee():
    employee_id = input("Enter employee ID: ").strip()
    if employee_id in staff_records:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()
    if not name or not department:
        print("Name and department cannot be empty.")
        return

    salary = float(input("Enter salary: "))
    if salary < 0:
        print("Salary cannot be negative.")
        return

    staff_records[employee_id] = {
        "name": name,
        "department": department,
        "salary": salary,
    }
    print("Employee added.")


def update_salary():
    employee_id = input("Enter employee ID: ").strip()
    if employee_id not in staff_records:
        print("Employee not found.")
        return

    new_salary = float(input("Enter new salary: "))
    if new_salary < 0:
        print("Salary cannot be negative.")
        return

    staff_records[employee_id]["salary"] = new_salary
    print("Salary updated.")


def delete_employee():
    employee_id = input("Enter employee ID: ").strip()
    if employee_id in staff_records:
        del staff_records[employee_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")


def search_employee():
    employee_id = input("Enter employee ID: ").strip()
    details = staff_records.get(employee_id)
    if details is None:
        print("Employee not found.")
    else:
        print(details)


def display_employee_reports():
    department_summary = {}
    for details in staff_records.values():
        department = details["department"]
        if department not in department_summary:
            department_summary[department] = {"payroll": 0, "count": 0}
        department_summary[department]["payroll"] += details["salary"]
        department_summary[department]["count"] += 1

    print("\nDepartment payroll and employee count:")
    for department, summary in department_summary.items():
        print(department, "Payroll:", summary["payroll"],
              "Employees:", summary["count"])

    top_paid = {}
    for details in staff_records.values():
        department = details["department"]
        if (department not in top_paid
                or details["salary"] > top_paid[department]["salary"]):
            top_paid[department] = details

    print("\nHighest-paid employee in each department:")
    for department, details in top_paid.items():
        print(department, ":", details["name"], details["salary"])

    print("\nEmployees sorted by salary:")
    salary_order = sorted(
        staff_records.items(),
        key=lambda entry: entry[1]["salary"],
        reverse=True,
    )
    for employee_id, details in salary_order:
        print(employee_id, details["name"], details["salary"])

    revised_records = {
        employee_id: {
            "name": details["name"],
            "department": details["department"],
            "salary": details["salary"] * 1.10,
        }
        for employee_id, details in staff_records.items()
        if details["salary"] < 50000
    }
    print("\nNew records with a 10% raise for salaries below 50000:")
    print(revised_records)

    department_totals = {}
    for details in staff_records.values():
        department = details["department"]
        if department not in department_totals:
            department_totals[department] = [0, 0]
        department_totals[department][0] += details["salary"]
        department_totals[department][1] += 1

    if department_totals:
        average_pay = {
            department: total / count
            for department, (total, count) in department_totals.items()
        }
        highest_average_department = max(average_pay, key=average_pay.get)
        print("\nDepartment with highest average salary:",
              highest_average_department,
              average_pay[highest_average_department])


def main():
    while True:
        print("\n--- EMPLOYEE DATABASE ---")
        print("1. Add employee")
        print("2. Update salary")
        print("3. Delete employee")
        print("4. Search employee")
        print("5. Show reports")
        print("6. Exit")

        option = input("Choose an option: ")
        if option == "1":
            add_employee()
        elif option == "2":
            update_salary()
        elif option == "3":
            delete_employee()
        elif option == "4":
            search_employee()
        elif option == "5":
            display_employee_reports()
        elif option == "6":
            print("Program closed.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
