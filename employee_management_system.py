# Fixed salary for each designation
designation_salary = {
    "manager": 30000,
    "developer": 25000,
    "trainee": 20000
}

# Load employees without using strip or split
def load_employees():
    employees = []
    try:
        f = open("employees.txt", "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.replace("\n", "")  # remove newline manually

            comma1 = line.find(',')
            comma2 = line.find(',', comma1 + 1)
            comma3 = line.find(',', comma2 + 1)

            name = line[:comma1]
            age = int(line[comma1+1:comma2])
            designation = line[comma2+1:comma3]
            salary = int(line[comma3+1:])

            emp = {
                "name": name,
                "age": age,
                "designation": designation,
                "salary": salary
            }
            employees.append(emp)
    except FileNotFoundError:
        pass

    return employees

# Save employees to file
def save_employees(employees):
    f = open("employees.txt", "w")
    for emp in employees:
        line = emp['name'] + "," + str(emp['age']) + "," + emp['designation'] + "," + str(emp['salary']) + "\n"
        f.write(line)
    f.close()

# Create account
def create_account(employees):
    while True:
        try:
            name = input("Enter employee name: ")
            age = int(input("Enter age (18 to 60): "))
            if age < 18 or age > 60:
                print("Age must be between 18 and 60.")
                continue

            print("Choose designation: manager / developer / trainee")
            designation = input("Enter designation: ").lower()
            if designation not in designation_salary:
                print("Invalid designation.")
                continue

            salary = designation_salary[designation]

            emp = {
                "name": name,
                "age": age,
                "designation": designation,
                "salary": salary
            }

            employees.append(emp)
            save_employees(employees)
            print("Account created successfully.\n")

            cont = input("Do you want to create another account? (yes/no): ").lower()
            if cont != "yes":
                break

        except ValueError:
            print("Invalid input! Please enter numbers only for age.\n")

# Display employees
def display_employees(employees):
    if not employees:
        print("No employee records found.\n")
        return

    print("\n--- Employee Details ---")
    for emp in employees:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Designation: {emp['designation']}, Salary: {emp['salary']}")
    print()

# Raise salary
def raise_salary(employees):
    name = input("Enter employee name to raise salary: ").lower()
    found = False

    for emp in employees:
        if emp['name'].lower() == name:
            found = True
            try:
                percent = float(input("Enter increment percentage (1 to 30): "))
                if percent < 1 or percent > 30:
                    print("Percentage must be between 1 and 30.")
                    return

                increment = emp['salary'] * (percent / 100)
                emp['salary'] += int(increment)
                save_employees(employees)
                print(f"Salary updated. New Salary: {emp['salary']}\n")
                return
            except ValueError:
                print("Invalid input! Enter a numeric value for percentage.")
                return

    if not found:
        print("Employee not found.\n")

# Main program
def main():
    employees = load_employees()

    while True:
        print("1. Create Account")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_account(employees)
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            raise_salary(employees)
        elif choice == '4':
            print("Thanks for using the application.")
            break
        else:
            print("Invalid choice. Please choose 1 to 4.\n")

# Run the program
main()
