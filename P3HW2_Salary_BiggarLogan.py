# CTI-110
# P3HW2 - Salary
# Logan Biggar
# 10/7/2021

name_employee = input("Enter Employee's name: ")
number_hours = float(input("Enter number of hours worked: "))
employee_pay = float(input("Enter Employee's Pay Rate: "))
overtime_hours = (number_hours-40)
reghour_pay = (employee_pay*40)
if number_hours > 40:
  overtimeRate = 1.5 * employee_pay
  overtime = (number_hours-40) * overtimeRate
  number_hours = 40
else:
  overtime = 0
gross_pay = reghour_pay + overtime
print("-----------------------------------------------")
print(name_employee)
print()
print("Hours Worked        Pay Rate        OverTime        OverTime Pay        RegHour Pay        Gross Pay")
print("----------------------------------------------------------------------------------------------------")
print(format(number_hours, ",.2f"), '              ', format(employee_pay, ",.2f"), '         ', format(overtime_hours, ",.2f"), '           ', format(overtime, ",.2f"), '           ', format(reghour_pay, ",.2f"), '         ', format(gross_pay, ",.2f"))
