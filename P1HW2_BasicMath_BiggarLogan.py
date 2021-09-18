tax_rate = 0.06
name_expense = input('Enter name of expense:')
monthly_charge = float(input('Enter monthly charge:'))
print('Bill:', name_expense, '-------','Before Tax:','$', format(monthly_charge, ",.2f"))
print()
monthly_tax = tax_rate * monthly_charge
print('Monthly Tax:','$', format(monthly_tax, ",.2f"))
monthly_charge_tax = monthly_tax + monthly_charge
print('Monthly Charge:', '$', format(monthly_charge_tax, ",.2f"))
annual_charge = monthly_charge_tax * 12
print('Annual Charge:', '$', format(annual_charge, ",.2f"))
