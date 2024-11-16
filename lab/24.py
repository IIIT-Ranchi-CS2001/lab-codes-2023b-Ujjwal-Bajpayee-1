def get_employee_data():
    employees = {}
    for _ in range(5):
        name = input("Enter employee name: ")
        salary = int(input(f"Enter salary for {name}: "))
        employees[name] = salary
    return employees

def sort_employees_by_salary(employees):
    employee_list = list(employees.items())
    for i in range(len(employee_list)):
        for j in range(0, len(employee_list) - i - 1):
            if employee_list[j][1] < employee_list[j + 1][1]:
                employee_list[j], employee_list[j + 1] = employee_list[j + 1], employee_list[j]
    return employee_list

def display_sorted_employees(sorted_employees):
    for rank, (name, salary) in enumerate(sorted_employees, start=1):
        print(f"{rank}. {name}: Rs. {salary}")

def main():
    employees = get_employee_data()
    sorted_employees = sort_employees_by_salary(employees)
    display_sorted_employees(sorted_employees)

if __name__ == "__main__":
    main()