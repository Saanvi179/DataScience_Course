employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Asha', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Ravi', 'age': 24, 'department': 'Development', 'salary': 45000}
}

def add_employee():
    
    while True:
        try:
            emp_id = int(input("Enter new Employee ID (integer): ").strip())
        except ValueError:
            print("Invalid input. Please enter a numeric Employee ID.")
            continue

        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            continue
        break

    name = input("Enter employee name: ").strip()
    # Age validation
    while True:
        try:
            age = int(input("Enter employee age: ").strip())
            if age <= 0:
                print("Age must be positive.")
                continue
            break
        except ValueError:
            print("Invalid age. Enter a number.")

    department = input("Enter employee department: ").strip()
    # Salary validation
    while True:
        try:
            salary = int(input("Enter employee monthly salary: ").strip())
            if salary < 0:
                print("Salary cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid salary. Enter a numeric value.")

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print(f"Employee with ID {emp_id} added successfully.\n")


def view_employees():
    
    if not employees:
        print("No employees available.\n")
        return

    header = f"{'ID':<6} {'Name':<20} {'Age':<5} {'Department':<15} {'Salary':<10}"
    print(header)
    print("-" * len(header))
    for emp_id, info in sorted(employees.items()):
        print(f"{emp_id:<6} {info['name']:<20} {info['age']:<5} {info['department']:<15} {info['salary']:<10}")
    print()  # blank line


def search_employee():
    
    try:
        emp_id = int(input("Enter Employee ID to search: ").strip())
    except ValueError:
        print("Invalid input. Employee ID must be a number.\n")
        return

    if emp_id in employees:
        info = employees[emp_id]
        print(f"Employee found (ID: {emp_id}):")
        print(f"Name      : {info['name']}")
        print(f"Age       : {info['age']}")
        print(f"Department: {info['department']}")
        print(f"Salary    : {info['salary']}\n")
    else:
        print("Employee not found.\n")


def main_menu():
    
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main_menu()
