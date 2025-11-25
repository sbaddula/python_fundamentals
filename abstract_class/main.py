from employee import FullTimeEmployee, PartTimeEmployee

def print_employee_info(employee):
    print(employee.describe_role(employee.name))
    print(f"Salary:  {employee.calculate_salary()}")


fulltime_employee = FullTimeEmployee("Martin", 5000)
print_employee_info(fulltime_employee)

parttime_employee = PartTimeEmployee("Luther", 20, 100)
print_employee_info(parttime_employee)

