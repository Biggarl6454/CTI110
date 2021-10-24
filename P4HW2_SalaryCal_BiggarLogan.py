# CTI-110
# P4HW2 - Salary Calculator
# Logan Biggar 
# 10/24/2021

emp_name = input("Enter employee's name or \"None\" to terminate: ")

count = 0
total_overtime = 0
total_reg_hours = 0
total_gross_pay = 0

while emp_name != 'None':
    HOURS_PER_WEEK = 40
    hours_worked = float(input("How many hours did "+emp_name+" worked? "))
    hourly_rate =  float(input("What is "+emp_name+"'s pay rate? "))
    
    if hours_worked >  HOURS_PER_WEEK:
        overtime = hours_worked - HOURS_PER_WEEK
    else:
        overtime = 0.0

    overtime_pay = hourly_rate * overtime
    reg_hour_pay = (hours_worked - overtime) * hourly_rate
    overtime_pay = overtime * hourly_rate * 1.5
    gross_pay = reg_hour_pay + overtime_pay

    print("Employee Name: "+emp_name)

    print("Hours Worked        Pay Rate             Overtime        Overtime Pay          RegHour Pay           Gross Pay")
    print("---------------------------------------------------------------------------------------------------------------")
    print(str(hours_worked)+"                "+str(hourly_rate)+"                  "+str(overtime)+"             "+str(overtime_pay)+"                  "+str(reg_hour_pay)+"                  "+str(gross_pay))

    count = count + 1
    total_overtime = total_overtime + overtime_pay
    total_reg_hours = total_reg_hours + reg_hour_pay
    total_gross_pay = total_gross_pay + gross_pay

    emp_name = input("Enter employee's name or \"None\" to terminate: ")

print("Total number of employees entered: "+str(count))
print("Total ammount payed for overtime: "+str(total_overtime))
print("Total ammount payed regular hours: "+str(total_reg_hours))
print("Total amount payed in gross: "+str(total_gross_pay))

input("Press any key to exit...")
