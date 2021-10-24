# CTI-110
# P4HW1 - Expenses
# Logan Biggar
# 10/23/2021

# get starting amount as user input. Input convert to float
start_amount = float(input("Enter starting amount in account $"))
# inital counter this will count the expense number
count = 1
# get the expenses and convert to float
expense = input("Enter expense "+str(count)+": ")
expense_amount = float(expense)
# check if user need to continue or not
option = input("Do you want to enter another expenses?(y/n) ")

# continue ask question till user user need to stop
while option != 'n':
    # increase the count 
    count = count + 1
    #get expense
    expense = input("Enter expense "+str(count)+": ")
    expense_amount = expense_amount + float(expense)
    option = input("Do you want to enter another expenses?(y/n) ")

# calculate balance
balance = start_amount - expense_amount

# print final statement
print("Amount in account before expenses substracted $"+str(start_amount))
print("Number of expenses entered: "+str(count))
print("Amount in account After expenses substracted is $"+str(balance))
print()

