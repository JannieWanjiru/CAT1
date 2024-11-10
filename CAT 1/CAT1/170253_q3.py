class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")


    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"{self.name}'s salary updated to {self.salary}.")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary}")
        return total_salary

    def display_all_employees(self):
        if self.employees:
            print(f"Employees in {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in {self.department_name} department.")

# sample functionality 
department = Department("Finance")

def company_management_system():
    while True:
        print("\nOptions: 1) Add Employee 2) Update Salary 3) Display All Employees 4) Display Total Expenditure 5) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            salary = float(input("Enter employee's salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)

        elif choice == "2":
            employee_id = input("Enter employee ID to update salary: ")
            new_salary = float(input("Enter new salary: "))
            employee = next((emp for emp in department.employees if emp.employee_id == employee_id), None)
            if employee:
                employee.update_salary(new_salary)
            else:
                print(f"No employee found with ID {employee_id}.")

        elif choice == "3":
            department.display_all_employees()

        elif choice == "4":
            department.calculate_total_salary_expenditure()

        elif choice == "5":
            print("Exiting the company management system.")
            break
        else:
            print("Invalid option, please try again.")

